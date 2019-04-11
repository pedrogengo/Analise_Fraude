import numpy as np

np.random.seed = 42

n_fraude = 5000
n_normal = 5000

renda_fraude = np.random.normal(1000,1250,n_fraude*2)
renda_fraude_retirados = renda_fraude[renda_fraude<700]
renda_fraude = np.setdiff1d(renda_fraude, renda_fraude_retirados)
valores_alem = np.random.choice(renda_fraude, renda_fraude.size - 5000, replace=False)
renda_fraude = np.setdiff1d(renda_fraude, valores_alem)
renda_normal = np.random.normal(1000,1250,n_normal*2)
renda_normal_retirados = renda_normal[renda_normal<700]
renda_normal = np.setdiff1d(renda_normal, renda_normal_retirados)
valores_alem = np.random.choice(renda_normal, renda_normal.size - 5000, replace=False)
renda_normal = np.setdiff1d(renda_normal, valores_alem)

valor_compra_fraude = np.random.normal(2000,500,n_fraude)
valor_compra_normal = np.random.normal(100,250,n_normal)

#https://www.terra.com.br/noticias/dino/a-cada-3-meses-o-brasileiro-gasta-cerca-de-r661-em-compras-pela-internet,70f7a51ef268f3648d98bec463372741o1lsr05w.html
media_gastos_fraude = np.random.normal(720,180,n_fraude)
media_gastos_normal = np.random.normal(220,250,n_normal*2)
media_gastos_normal_retirados = media_gastos_normal[media_gastos_normal<=0]
media_gastos_normal = np.setdiff1d(media_gastos_normal, media_gastos_normal_retirados)
valores_alem = np.random.choice(media_gastos_normal, media_gastos_normal.size - 5000, replace=False)
media_gastos_normal = np.setdiff1d(media_gastos_normal, valores_alem)


'''Categorias:
   1->Eletronicos e Celulares
   2->Eletrodomesticos
   3->Informatica e Games
   4->Outros
   5->Vestimenta
   6->Saude e beleza'''
#https://novonegocio.com.br/empreendedorismo/produtos-mais-vendidos-internet//}     
categoria_compra_fraude = np.random.rand(n_fraude)
categoria_compra_fraude[categoria_compra_fraude <= 0.55] = 1
categoria_compra_fraude[categoria_compra_fraude <= 0.8] = 2
categoria_compra_fraude[categoria_compra_fraude <= 0.9] = 3
categoria_compra_fraude[categoria_compra_fraude < 1] = 4

categoria_compra_normal = np.random.rand(n_normal)
categoria_compra_normal[categoria_compra_normal <= 0.4] = 1
categoria_compra_normal[categoria_compra_normal <= 0.65] = 3
categoria_compra_normal[categoria_compra_normal <= 0.8] = 5
categoria_compra_normal[categoria_compra_normal <= 0.85] = 6
categoria_compra_normal[categoria_compra_normal <= 0.9] = 2
categoria_compra_normal[categoria_compra_normal < 1] = 4

#https://ecommercenews.com.br/noticias/pesquisas-noticias/brasil-tem-horario-de-pico-de-compras-online-das-12h-as-14-diz-pesquisa/
horario_compra_fraude = np.random.normal(13,3,n_fraude);
horario_compra_normal = np.random.normal(13,3,n_normal);

compra_parcelada_fraude = np.zeros(n_fraude)
compra_parcelada_normal = np.zeros(n_normal)
compra_parcelada_normal[0:int(n_normal/2)] = 1
np.random.shuffle(compra_parcelada_normal)

X_normal = np.vstack([renda_normal, media_gastos_normal, valor_compra_normal, categoria_compra_normal, horario_compra_normal, compra_parcelada_normal]).T
X_fraude = np.vstack([renda_fraude, media_gastos_fraude, valor_compra_fraude, categoria_compra_fraude, horario_compra_fraude, compra_parcelada_fraude]).T

X = np.vstack ([ X_normal , X_fraude ])

y = np.array ([0] * n_normal + [1] * n_fraude )