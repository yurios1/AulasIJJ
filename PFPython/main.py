from projetoFinal import criarUsuario, logarUsuario, verToken, convToCSV, bdUsuarios

CUser = criarUsuario()

ULogin = logarUsuario(CUser)

token = verToken(ULogin)

bd = convToCSV(bdUsuarios)
print()