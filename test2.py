import ktrain
p = ktrain.load_predictor('model_BERT')
f=open('text.txt','r')
txt = f.read()
f.close()
output = p.predict(txt)
print(output)


