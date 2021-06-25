"""char_util"""
# TIL https://pypi.org/project/Unidecode/ but it is GPL2 and is mapping tables
# http://semplicewebsites.com/sites/default/files/latinise_compact.js_.txt
# 
import unicodedata


def discovery(tests):
    """Input a list of strings and reveal unicode details."""
    for test in tests:
        print(f"Testing /{test}/")
        for c in test:
            uni = unicodedata.name(c)
            dec = ord(c)
            print(f"/{c}/ ({dec}) {uni}")
            decomp = unicodedata.decomposition(c)
            print(f"decomp /{c}/ {decomp}")
            nfkd_form = unicodedata.normalize("NFKD", c)
            for c1 in nfkd_form:
                combo = unicodedata.combining(c1)
                print(f"combo /{c1}/ {combo}")
                decomp = unicodedata.decomposition(c1)
                print(f"decomp /{c1}/ {decomp}")
            # https://stackoverflow.com/questions/8935111/translating-letters-not-in-7bit-ascii-to-ascii-like-%C5%84-to-n-and-%C4%85-to-a
            try:
                cname = uni[:uni.index(' WITH')]
                print (unicodedata.lookup(cname))
            except (ValueError, KeyError):
                print(f"Failed to find base letter of {uni} with WITH")
            try:
                cname = uni.split()[-1]
                if "SHARP" in uni:
                    cname = "".join([ch*2 for ch in cname])
                if "SMALL" in uni:
                    cname = cname.lower()
                print(f"I think base letter is /{cname}/")
            except (ValueError, KeyError):
                print(f"Failed to find base letter of {uni} with last word")         
if __name__ == "__main__":  # pragma: no cover
    # setup()
    tests = [
        # "ł",
        # "ø",
        "ß",
        "ẞ",
        # "ü",
        # "ȕ",
        # "à",
        # "á",
        # "â",
        # "ã",
        # "ä",
        # "ó",
        "æ",
        # where is "ue", "oe" liason?
        # "å",
        # other liason "ng" "hv"? "oi" 
    ]
    discovery(tests)
