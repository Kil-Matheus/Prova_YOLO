# Prova_YOLO
Após fazer as análises do próprio github fornecido pela prova 
https://github.com/rmnicola/p2-pratica

O código praticamente faz o seguinte.
Ele importa o cv2 e o ultralytics

importa o vídeo
importa o modelo, esse documento 'yolo8vn.pt' é um dataset puro, sem nenhum treinamento, onde eu puxei do site 'https://universe.roboflow.com/project-pfubb/face-detectio/model/3' e tentei treina-lo usando a o código de uma das ponderadas minhas que eu fiz utilizando o Colab, poderada 3 se não me lembro. Infelizmente e deu algum erro que eu desconheço, mas ele gerou esse arquivo 'yolo8vn.pt' que eu usei no modelo.

Dentro do for, eu coloquei para ler o vídeo, o modelo sobreescreve o vídeo com o retângulo detectando as pessoas, onde ao mesmo tempo eu gravo o vídeo frame a frame, existe uma condição onde se você clicar 'q' ele saiu do vídeo.

E após toda a execução do mesmo, ele fecha todas as janelas e gera uma imagem de um ônibus, não sei o porque.