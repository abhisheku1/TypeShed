import _win32typing
from pywintypes import IID as IID

def BindIFilterFromStorage(*args, **kwargs): ...  # incomplete
def BindIFilterFromStream(*args, **kwargs): ...  # incomplete
def LoadIFilter(*args, **kwargs): ...  # incomplete

CHUNK_EOC: int
CHUNK_EOP: int
CHUNK_EOS: int
CHUNK_EOW: int
CHUNK_NO_BREAK: int
CHUNK_TEXT: int
CHUNK_VALUE: int
FILTER_E_ACCESS: int
FILTER_E_EMBEDDING_UNAVAILABLE: int
FILTER_E_END_OF_CHUNKS: int
FILTER_E_LINK_UNAVAILABLE: int
FILTER_E_NO_MORE_TEXT: int
FILTER_E_NO_MORE_VALUES: int
FILTER_E_NO_TEXT: int
FILTER_E_NO_VALUES: int
FILTER_E_PASSWORD: int
FILTER_S_LAST_TEXT: int
IFILTER_FLAGS_OLE_PROPERTIES: int
IFILTER_INIT_APPLY_INDEX_ATTRIBUTES: int
IFILTER_INIT_APPLY_OTHER_ATTRIBUTES: int
IFILTER_INIT_CANON_HYPHENS: int
IFILTER_INIT_CANON_PARAGRAPHS: int
IFILTER_INIT_CANON_SPACES: int
IFILTER_INIT_HARD_LINE_BREAKS: int
IFILTER_INIT_INDEXING_ONLY: int
IFILTER_INIT_SEARCH_LINKS: int
IID_IFilter: _win32typing.PyIID
