
def likings(likes):

    # len_likes = len(likes)
    if len(likes)==0:
        print("No one likes it...yet")
    elif len(likes)==1:
        print(likes[0] + " like it")
    elif len(likes)==2:
        print(likes[0]+ " and " + likes[1] + " like it")
    elif len(likes)==3:
        print(likes[0]+ "," + likes[1]+ " and "+likes[2]+ " like it")
    else:
        print(likes[0]+ "," + likes[1]+"," + str(int(len(likes))-2) + " likes it")


names = ["Peter","Ana","Mark","Dale","Peter"]
likings(names)