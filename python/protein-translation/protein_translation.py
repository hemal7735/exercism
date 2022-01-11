def proteins(strand):
    ans = []
    
    codes = [strand[i:i+3] for i in range(0, len(strand), 3)]

    print(codes)

    mapping = get_map()

    for code in codes:
        p = mapping[code]

        if p == "STOP":
            break
        else:
            ans.append(p)
    
    return ans

def get_map():
    code_to_protien = {}
    code_to_protien["AUG"] = "Methionine"
    
    code_to_protien["UUU"] = "Phenylalanine"
    code_to_protien["UUC"] = "Phenylalanine"

    code_to_protien["UUA"] = "Leucine"
    code_to_protien["UUG"] = "Leucine"

    code_to_protien["UCU"] = "Serine"
    code_to_protien["UCC"] = "Serine"
    code_to_protien["UCA"] = "Serine"
    code_to_protien["UCG"] = "Serine"

    code_to_protien["UAU"] = "Tyrosine"
    code_to_protien["UAC"] = "Tyrosine"

    code_to_protien["UGU"] = "Cysteine"
    code_to_protien["UGC"] = "Cysteine"

    code_to_protien["UGG"] = "Tryptophan"

    code_to_protien["UAA"] = "STOP"
    code_to_protien["UAG"] = "STOP"
    code_to_protien["UGA"] = "STOP"

    return code_to_protien