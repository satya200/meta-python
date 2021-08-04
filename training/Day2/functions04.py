
def outerFun(greet):

    def innerFun(design):

        def innerMostFun(gname):
            print(greet, design, gname)

        return innerMostFun

    return innerFun

outerFun("Welcome")("----->")("Sachin")

designFun = outerFun("Greetings")
nameFun = designFun("====>>")

nameFun("Rahul")
nameFun("Sourav")
nameFun = designFun("*****>")
nameFun("Sehwag")

