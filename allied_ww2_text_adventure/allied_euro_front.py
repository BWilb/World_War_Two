import charles_ai
import churchill_ai
import fdr_ai

def allied_ww2():
    print("FDR and his army will be transferred to Washington DC.")
    fdr_ai.main()

    print("Churchill will be transferred to London.")
    churchill_ai.main()

    print("Charles De Gaulle will be transferred to Africa.")
    charles_ai.main()

def main():
    allied_ww2()