# Use an LLM like OpenAI's GPT or any other language model
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma

import logging
from typing import List
from langchain.chains import LLMChain


class CompliantChecker:
    def __init__(self, chunk_size=500, chunk_overlap=100):
        prompt = PromptTemplate(template="""
        Given a text from a website, you need to check if its is complaint against the context provided. Answer in the following format:
        status: Complaint/Non-Complaint/NA
        Note:
        Segment is a website content, do in case if it is not relevant to context just give NA.
        reason: Reason for why it's non complaint, give proper reason. 
        
        Context: {context}
        Segment: {segment}
        Answer: 
        """, input_variables=["context", "segment"])
        llm = ChatOpenAI(temperature=0)  # Default turbo model
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=" ")
        self.call_llm = LLMChain(llm=llm, prompt=prompt)

    def _get_segments(self, text: str) -> List[str]:
        segments = text.split("\n")
        print(len(segments))
        return [segment for segment in segments if len(segment.split(" ")) > 3] # minium 4 words

    def _index_chunk(self, policy_content: str):
        # Load the document, split it into chunks, embed each chunk and load it into the vector store.
        print("Indexing policy content to Vector DB")
        policy_chunks = self.text_splitter.split_text(policy_content)
        db = Chroma.from_texts(policy_chunks, OpenAIEmbeddings())
        return db

    def analyze_compliance(self, policy_content: str, target_content: str) -> List[str]:
        print("Analyzing compliance...")
        db = self._index_chunk(policy_content)

        findings = []
        for i, segment in enumerate(self._get_segments(target_content)[:10]):
            print("Checking...", i)
            docs = db.similarity_search(query=segment, k=5)
            context = "\n\n".join([doc.page_content for doc in docs])
            findings.append(self.call_llm.predict(segment=segment, context=context))

        return findings
        #     if "some non-compliant issue" in target_content:
        #         findings.append(ComplianceFinding(
        #             compliant=False,
        #             reason="Non-compliant issue found",
        #             recommended_changes="Make specific changes to comply"
        #         ))
        #     # Your logic here
        # return findings
