import pickle

f=open("ref_name.pkl","rb")
ref_dictt=pickle.load(f)         
f.close()

f=open("ref_embed.pkl","rb")
embed_dictt=pickle.load(f)     
f.close()

print(ref_dictt)
print(embed_dictt.keys())

print("---------------------------------------")

# del ref_dictt['1']
del embed_dictt['1']
# ref_dictt.clear()
# embed_dictt.clear()

f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f)
f.close()

f=open("ref_embed.pkl","wb")
pickle.dump(embed_dictt,f)
f.close()

f=open("ref_name.pkl","rb")
ref_dictt=pickle.load(f)         
f.close()

f=open("ref_embed.pkl","rb")
embed_dictt=pickle.load(f)      
f.close()

print(ref_dictt)
print(embed_dictt.keys())
