import allied_classes
import charles_ai
import churchill_ai
import fdr_ai

def allied_ww2():
    print("FDR and his army will be transferred to Washington DC.")
    fdr = allied_classes.FDR()
    fdr_ai.main(fdr)

    print("Churchill will be transferred to London.")
    churchill = allied_classes.WinstonChurchill()
    churchill_ai.main(churchill)

    print("Charles De Gaulle will be transferred to Africa.")
    charles = allied_classes.CharlesDeGaulle()
    charles_ai.main(charles)

def main():
    allied_ww2()