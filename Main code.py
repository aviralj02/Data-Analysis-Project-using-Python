import pandas as pd
import matplotlib.pyplot as p
import time
print(' '*15,"DATA ANALYSIS OF POPULATION OF INDIA")
print(' '*15,'-'*36)
msg='All the data of population of India in this programme is according to 2011 census.\nNOTE: Python is case-SENSITIVE so type exact State or Union Terrritory name wherever required.'
for x in msg:
    print(x,end='')
    time.sleep(0.001)
next=input('\nPress Enter to continue....')

while(True):
    print('\nMain Menu')
    print('-'*10)
    print('1. Fetch Data')
    print('2. Dataframe Statistics')
    print('3. Display Records')
    print('4. Working on Records')
    print("5. Working on Columns")
    print("6. Search specific row/column")
    print("7. Data Visualization")
    print("8. Made By")
    ch=int(input("Enter your choice: "))
    if ch==1:
        df=pd.read_csv("C:\\Users\\Aviral\\Desktop\\IP Project\\CSV.csv")
        dp=df.set_index('State and UT')
    elif ch==2:
        while(True):
            print("\nDataframe Statistics Menu")
            print('-'*28)
            print("1. Display the Transpose")
            print("2. Display all column names")
            print("3. Display the indexes")
            print("4. Display the shape")
            print("5. Display the dimension")
            print("6. Display the data types of all columns")
            print("7. Display the size")
            print("8. Display Dataframe")
            print("9. Exit")
            ch2=int(input("Enter choice: "))
            if ch2==1:
                print(dp.T)
            elif ch2==2:
                print(df.columns)
            elif ch2==3:
                print(dp.index)
            elif ch2==4:
                print(df.shape)
            elif ch2==5:
                print(dp.ndim)
            elif ch2==6:
                print(df.dtypes)
            elif ch2==7:
                print(df.size)
            elif ch2==8:
                print(df)
            elif ch2==9:
                break
    elif ch==3:
        while(True):
            print('\nDisplay Records menu')
            print('-'*22)
            print("1. Top 5 Records")
            print("2. Bottom 5 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Details of a specific State or Union territory")
            print("6. Exit")
            ch3=int(input("Enter choice: "))
            if ch3==1:
                print(df.head())
            elif ch3==2:
                print(df.tail())
            elif ch3==3:
                n=int(input('Enter how many records you want to display from the top: ')) 
                print(df.head(n))
            elif ch3==4:
                z=int(input('Enter how many records you want to display from the top: '))
                print(df.tail(z))
            elif ch3==5:
                print(dp.index)
                st=input("Enter the state or union territory name: ")
                print(dp.loc[st])
            elif ch3==6:
                break
    elif ch==4:
        while(True):
            print('\nWorking on Records Menu: ')
            print('-'*27)
            print('1. Delete a specific state record')
            print('2. Update a specific state record')
            print('3. Exit')
            ch4=int(input('Enter a choice: '))
            if ch4==1:
                a=input('Enter state name whose data needs to be deleted: ')
                dp.drop([a],inplace=True)
                print('Data deleted successfully')
            elif ch4==2:
                a=input("Enter state name whose data needs to be updated: ")
                b=int(input("Enter new Population: "))
                c=int(input("Enter new number of Rural population: "))
                d=int(input("Enter new number of Urban population: "))
                e=int(input("Enter new Area of state: "))
                f=int(input("Enter new Male population: "))
                g=int(input("Enter new Female population: "))
                h=int(input("Enter new sex ratio: "))
                dp.loc[a]=[b,c,d,e,f,g,h]
                print('Data updated successfully')
                dis=input('Display updated Dataframe(YES/NO): ')
                while(True):
                    if dis=='YES':
                        print(dp)
                        break
                    elif dis=='NO':
                        break
            elif ch4==3:
                break
    elif ch==5:
        while(True):
            print('\nWorking on Columns Menu')
            print('-'*25)
            print("1. Insert a new column data")
            print("2. Delete a specific column")
            print('3. Exit')
            ch5=int(input('Enter a choice: '))
            if ch5==1:
                print('NOT ALLOWED')
            elif ch5==2:
                a=input('Enter column name which needs to be deleted: ')
                df.drop([a],axis=1,inplace=False)
                print('Column Temporary deleted')
            elif ch5==3:
                break
    elif ch==6:
        while(True):
            print('\nSearch Menu')
            print('-'*14)
            print("1. Search for the details of a specific state or UT")
            print("2. Search details of a specific column")
            print("3. Exit")
            ch6=int(input('Enter a choice: '))
            if ch6==1:
                print(dp.index)
                st=input("Enter the name of the state or UT whose details you want to see: ")
                print(dp.loc[st])
            elif ch6==2:
                print(df.columns)
                col=input("Enter column name whose details you want to see: ")
                print(dp[col])
            elif ch6==3:
                break
    elif ch==7:
        while(True):
            print('\nData Visualization Menu')
            print('-'*24)
            print('1. Bar Plot')
            print('2. Pie chart')
            print('3. Exit')
            ch7=int(input('Enter a choice: '))
            if ch7==1:
                while(True):
                    print('1. Total Population bar plot')
                    print('2. Rural-Urban population bar plot')
                    print('3. Male-Female population bar plot')
                    print('4. Area plot')
                    print('5. Sex ratio plot')
                    print('6. Exit')
                    ch71=int(input('Enter a choice: '))
                    if ch71==1:
                        pop=dp['Population']
                        sut=dp.index
                        p.barh(sut,pop,label='Total Population')
                        p.ylabel('States and UTs')
                        p.xlabel('Population')
                        p.title('Population graph of states and UTs')
                        p.xticks()
                        p.legend()
                        p.grid(True)
                        p.show()
                    elif ch71==2: ##############################################
                        rp=dp['Rural population']
                        up=dp['Urban population']
                        sut=dp.index
                        p.barh(sut,rp,label='Rural Population',color='y')
                        p.barh(sut,up,label='Urban Population',color='m')
                        p.xlabel('Population')
                        p.ylabel('States and UT')
                        p.xticks()
                        p.yticks()
                        p.legend()
                        p.grid(True)
                        p.show()
                    elif ch71==3:
                        mp=dp['Male population']
                        fp=dp['Female population']
                        sut=dp.index
                        p.barh(sut,mp,label='Male Population',color='b')
                        p.barh(sut,fp,label='Female Population',color='pink')
                        p.xlabel('Population')
                        p.ylabel('States and UT')
                        p.xticks()
                        p.yticks()
                        p.legend()
                        p.grid(True)
                        p.show()
                    elif ch71==4:
                        ar=dp['Area(km2)']
                        sut=dp.index
                        p.barh(sut,ar)
                        p.xlabel('Area in square km')
                        p.ylabel('States and UT')
                        p.xticks()
                        p.grid(True)
                        p.show()
                    elif ch71==5:
                        sr=dp['Sex ratio']
                        sut=dp.index
                        p.barh(sut,sr)
                        p.xlabel('Sex ratio')
                        p.ylabel('States and UT')
                        p.xticks()
                        p.grid(True)
                        p.show()
                    elif ch71==6:
                        break
            elif ch7==2:
                while(True):
                    print('1. Total Population pie chart')
                    print('2. Rural population pie chart')
                    print('3. Urban population pie chart')
                    print('4. Male population pie chart')
                    print('5. Female population pie chart')
                    print('6. Area pie chart')
                    print('7. Sex ratio pie chart')
                    print('8. Exit')
                    ch72=int(input('Enter a choice: '))
                    if ch72==1:
                        pop=dp['Population']
                        sut=dp.index
                        p.pie(pop,labels=sut)
                        p.title('Total Population Pie chart')
                        p.legend()
                        p.show()
                    elif ch72==2:
                        rp=dp['Rural population']
                        sut=dp.index
                        p.pie(rp,labels=sut)
                        p.title('Rural Population pie chart')
                        p.legend()
                        p.show()
                    elif ch72==3:
                        up=dp['Urban population']
                        sut=dp.index
                        p.pie(up,labels=sut)
                        p.title('Urban Population Pie chart')
                        p.legend()
                        p.show()
                    elif ch72==4:
                        mp=dp['Male population']
                        sut=dp.index
                        p.pie(mp,labels=sut)
                        p.title('Male population pie chart')
                        p.legend()
                        p.show()
                    elif ch72==5:
                        fp=dp['Female population']
                        sut=dp.index
                        p.pie(fp,labels=sut)
                        p.title('Female population pie chart')
                        p.legend()
                        p.show()
                    elif ch72==6:
                        ar=dp['Area(km2)']
                        sut=dp.index
                        p.pie(ar,labels=sut)
                        p.title('Area covered by states and UTs pie chart')
                        p.legend()
                        p.show()
                    elif ch72==7:
                        sr=dp['Sex ratio']
                        sut=dp.index
                        p.pie(sr,labels=sut)
                        p.title('Sex ratio pie chart')
                        p.legend()
                        p.show()
                    elif ch72==8:
                        break
            elif ch7==3:
                break
    elif ch==8:
        print('Name : Aviral Jain')
        next=input('Press Enter to go back to Main Menu........')
        
                              
                              
                    
                        
                        
                    
            
                                                  
                        
                        
                              
                
                    
                
                    
                
           
                    
                  
        
                
    


