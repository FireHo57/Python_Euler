

if __name__=="__main__":
    numbers_to_nine={"one","two","three","four","five",
                         "six","seven","eight","nine"}
    ten_to_twenty={"ten","eleven","twelve","thirteen","fourteen",
                   "fifteen","sixteen","seventeen","eighteen","nineteen"}
    tens={"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"}

    #numbers in 1-19
    letters_to_nine=0
    for i in numbers_to_nine:
        letters_to_nine+=len(i)

    letters_in_teens=0
    for i in ten_to_twenty:
        letters_in_teens+=len(i)

    letters_in_hundred=0
    for i in tens:
        letters_in_hundred+=(10*len(i))+(letters_to_nine*9)

    letters_in_hundred+=letters_to_nine+letters_in_teens

    letters_in_thousand=0
    hundred=len("hundred")
    for i in numbers_to_nine:
        letters_in_thousand+=(len(i)+3)*100+hundred+letters_in_hundred

    letters_in_thousand+=len("onethousand")

    print letters_in_thousand

