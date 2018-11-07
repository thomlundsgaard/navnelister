
def ordn_grupper(børn, stue: list):
    rød=[];
    gul=[];
    blå=[];
    for tæller in range(len(børn)):
        if stue[tæller]=='Rød stue': rød.append(børn[tæller]);
        if stue[tæller]=='Blå stue': blå.append(børn[tæller]);
        if stue[tæller]=='Gul stue': gul.append(børn[tæller]);
    gul.insert(0, str(len(gul)-1));
    rød.insert(0, str(len(rød)-1));
    blå.insert(0, str(len(blå)-1));
    ordnet_liste = [rød, blå, gul];
    return ordnet_liste;


børn = [];
stue = [];
status='intet';

with open('test.dat','r') as fil :
    data=fil.readlines();
    data = [x.strip() for x in data]; 
for line in data:
    if line=='' : status='intet';
    elif line=='Navn' : status='navn';
    elif line=='Stue' : status='stue';
    elif line=='Fødselsdag': status='dato';
    if status=='navn':
        børn.append(line.split()[0]);
    elif status=='stue': stue.append(line); 
resultat=ordn_grupper(børn, stue);

print(' <!DOCTYPE html><html><head> <meta charset="utf-8"/><link rel="stylesheet" type="text/css" href="test.css"><head><body><div ><h3 style="color:red;">Rød stue</h3><p>');
for x in resultat[0]:
    print(x+'<br>');
print('</p></div><div><h3 style="color:blue;">Blå stue</h3><p>');    
for x in resultat[1]:
    print(x+'<br>');
print('</p></div><div><h3 style="color:yellow;">Gul stue</h3><p>');    

for x in resultat[2]:
    print(x+'<br>');
print('</p></div></body></html>');    


