from pydantic import BaseModel, Field

class RawArticles(BaseModel):
    descricao: str = Field(..., min_length=5, max_length=250)
    linkpdf:   str = Field(..., min_length=0, max_length=250)
    linkhtml:  str = Field(..., min_length=0, max_length=250)

class RawAuthors(BaseModel):
    artigos: str = Field(..., min_length=5, max_length=250)
    nomes: str = Field(..., min_length=0)
