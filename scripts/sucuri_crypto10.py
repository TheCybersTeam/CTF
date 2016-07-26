#coding: utf-8 -*-

# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# By: 	    Offset
# Greats:   RATF, Ninja
# Version:  1.1

# Description: Get all upper cases strings and numbers from the text.
# 1- Result: KNEE1988G62QIZMFIRKSKJHVESKT1441KRAVGIL5
# 2- Remove "1988" end "1441" from result.
# 3 - echo "KNEEG62QIZMFIRKSKJHVESKTKRAVGIL5" | base32 -d

texto = "o departamento de políKia federal (dpf), ou simplesmeNtE polícia fEderal (pf), é uma instituição policial brasileira, subordinada ao ministério da justiça, cuja função, de acordo com a constituição de 1988, é exercer a seGurança pública p6r2 a preservação da ordem pública Que da IncolumidadeZ das pessoas, beM como dos bens e interesses da união, exercendo atividades de polícia marítima, aeroportuária e de FronteIras, Repressão Kao tráfico de entorpecenteS, Kontrabando e descaminho, e exercendo com exclusividade as funções de polícia Judiciária da Hunião.Va polícia fEderal, deS aKordo com o arTigo 144, parágrafo 1º, da Konstituição fedeRal, é instituídA por lei como órgão Vermanente, orGanIzado e mantido peLa união e e5truturado em carreira."
pesquisa = "ABCDEFGHIJKLMNOPQRSTUVXZ0123456789"
res = ""
for i in texto:
	if i in pesquisa:
		res+=i

print res


