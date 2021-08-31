
#criando a lista
janela=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
corredor=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
i=0
janela[i]=0
corredor[i]=0
c=0
while True:
	print("-="*30)
	print('''\033[0;31;40m1- comprar passagem\033[m
\033[0;33;40m2- mapa das cadeira\033[m
\033[0;36;40m3- encerrar seção\033[m
	''')
	print("-="*30)
	opcao=int(input("o que você deseja fazer? \033[0;32;40m"))
	print("\033[m")
#janela e corredores
	if opcao == 1:
		print("-="*30)
		print("comprar passagem")
		opcao_local=input("[ j ] para janela e [ c ] para corredor ").lower()
		opcao_poltrona=int(input("em qual poltrona vc deseja ficar? "))
#para poltrona livre e ocupada
		if opcao_local == "j" and opcao_poltrona in janela:
			print("\033[0;32;40mcompra sucedida\033[m")
			index= janela.index(opcao_poltrona)
			removido=janela.pop(index)
			janela[i]=1
		elif opcao_local == "j" and opcao_poltrona == removido:
			print("\033[0;31;40mpoltrona ocupada\033[m")
		
		if opcao_local =="c" and opcao_poltrona in corredor:
			print("\033[0;33;40mcompra sucedida\033[m")
			index=corredor.index(opcao_poltrona)
			removido=corredor.pop(index)
			corredor[i]=1
		elif opcao_local == "c" and opcao_poltrona == removido:
			print("\033[0;31;40mpoltrona ocupada\033[m")
	
#mostrar mapa	
	if opcao == 2:
		print("janela \t\t\t corredor")
		for c in range(1,25):
			if janela[i] == 0 and corredor[i] == 0:
				print("{} livre \t\t {} livre".format(c,c))
			elif janela[i]== 0 and corredor[i]==1:
				print("{} livre \t\t {} ocupado".format(c,c))
			elif janela[i]== 1 and corredor[i]==1:
				print("{} ocupado \t\t {} ocupado".format(c,c))
			elif janela[i]== 1 and corredor[i]==0:
				print("{} ocupado \t\t {} livre".format(c,c))
	
	
	if opcao == 3:
			break
			
