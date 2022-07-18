from fileinput import filename
import os

from reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}

class Reader: 
    def __init__(self,filename) -> None:
        extension = os.path.splittext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self) -> None:
        self.f.close()

    def read(self) -> str:
        return self.f.read() 
