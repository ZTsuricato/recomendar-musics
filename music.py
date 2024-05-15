musicas = [
    ("Musica 1", "Rock"),
    ("Musica 2", "Pop"),
    ("Musica 3", "jazz"),
    ("Musica 4", "Rock"),
    ("Musica 5", "Pop"),
]

 # Histórico de musicas ouvidas pelo usuário
historico_usuario = ["Rock", "jazz", "Pop", "jazz", "Pop"]


# funçao para recomendar musicas
def recomendar_musica(historico):
  # contar a frequencia de cada gênero no historico 
   frequencia = {}
   for genero in historico:
     if genero in frequencia:
       frequencia[genero] += 1
     else:
       frequencia[genero] = 1

       # Encontrar o gênero mais frequente 
       genero_mais_frequente = max(frequencia, key=frequencia.get)

       #Recomendar musicas desse gênero
       recomendacoes = []
       for titulo, genero in musicas:
          if genero == genero_mais_frequente:
            recomendacoes.append(titulo)
       return recomendacoes


# obter recomendações para usuario 
recomendacoes_usuario = recomendar_musica(historico_usuario)
print("Musicas recomendadas:", recomendacoes_usuario)
         