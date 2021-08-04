
def outerFun(fnc):

    def helperFun():
        print("=" * 40)
        print("Logging into the service.....")
        fnc()
        print("Logging out of the service....")
        print("=" * 40)

    return helperFun

@outerFun       # debitFun = outerFun(debit); debitFun()
def debit():
    print("Debit called....")
    print("Amount Successfully debited from the account")

@outerFun
def credit():
    print("Credit called.....")
    print("Amount Successfully credited into the account")

@outerFun
def transfer():
    print("Trasfer called.....")
    print("Amount Successfully transferred from the account")

debit()
credit()
transfer()