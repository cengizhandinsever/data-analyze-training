# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:51:58 2023

@author: dinse
"""
import pandas as pd 
df=pd.read_csv('ds_salaries.csv')
df.head()
df.columns
"""
Index(['work_year', 'experience_level', 'employment_type', 'job_title',
       'salary', 'salary_currency', 'salary_in_usd', 'employee_residence',
       'remote_ratio', 'company_location', 'company_size'],
      dtype='object')
"""
df.work_year
df.experience_level.value_counts()
df[df.experience_level == "SE"]["salary"].mean()
df[df.experience_level == "MI"]["salary"].mean()
df[df.experience_level == "EN"]["salary"].mean()
df[df.experience_level == "EX"]["salary"].mean()
df.job_title
df.job_title.value_counts()
df[df["job_title"]== "Data Analyst"]["salary"].mean()
df[df.salary == df.salary.max()]
df.job_title

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import seaborn as sns

# Meslek gruplarına göre ortalama maaşları hesaplama
meslek_gruplari = df.groupby('job_title')['salary'].mean().head(20)

# Histogram grafiği oluşturma
plt.bar(meslek_gruplari.index, meslek_gruplari)

# Eksen etiketlerini güncelleme
plt.xlabel("Meslek Grupları")
plt.ylabel("Ortalama Maaşlar")

# Grafik başlığını ekleme
plt.title("Meslek Gruplarına Göre Ortalama Maaşlar")

# Grafiği ekranda gösterme
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
###############################################################################

tecrübe = df.groupby("experience_level")["salary"].mean()
plt.bar(tecrübe.index,tecrübe,color = ["red","yellow","orange","purple"])
plt.xlabel("tecrübe seviyesi")
plt.ylabel("ortalama maaş")
plt.title("tecrübe seviyesine göre ortalama maaşlar")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
###############################################################################
df.isnull().sum()#boş değer yok
df.head(10)
df.company_location.value_counts()
df[(df.job_title == "Data Scientist")&(df.company_location == "US")]["salary"].mean()#and sorgusu
df[(df.job_title == "Data Scientist")&(df.company_location == "CL")]["salary"].mean()
###############################################################################
# Sadece Veri Analistleri'ni seçin
veri_analistleri = df[df["job_title"] == "Data Scientist"]

# Şirket lokasyonlarına göre gruplayın ve ortalama maaşları hesaplayın
ortalama_maaslar = veri_analistleri.groupby("company_location")["salary"].mean()

# Histogram grafiği oluşturun
plt.bar(ortalama_maaslar.index, ortalama_maaslar)

# Eksen etiketlerini güncelleyin
plt.xlabel("Şirket Lokasyonları")
plt.ylabel("Ortalama Maaşlar")

# Grafik başlığını ekleyin
plt.title("Veri Analistleri: Şirket Lokasyonlarına Göre Ortalama Maaşlar")

# Eksen etiketlerini döndürün
plt.xticks(rotation=45)

# Grafiği ekranda gösterin
plt.show()


