class Login:
    def __init__(info, user = "", password = ""):  
        info.user = user
        info.password = password

class User:
   def __init__(infouser, userName  = "", passw  = "", id = "", name  = "", lastname  = ""):
        infouser.userName = userName
        infouser.passw = passw
        infouser.id = id
        infouser.name = name
        infouser.lastname = lastname

class Account:
     def __init__(infoAccount  = "", iden  = "", num_account  = "", balance  = "", balance2 = "", num_account2 = ""):
        infoAccount.iden =iden
        infoAccount.num_account = num_account
        infoAccount.num_account2 =num_account2
        infoAccount.balance = balance
        infoAccount.balance2 = balance2
