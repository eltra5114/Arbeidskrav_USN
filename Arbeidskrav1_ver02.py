#!/usr/bin/env python
# coding: utf-8

# <h3>Arbeidskrav 1 - sammenligne årlige kostnader av elbil og bensinbil</h3>
# Elena Tranvåg (eltra5114@usn.no)
# Sist oppdatering: 2025 - 09 - 23

# In[7]:


km_p_år = 10000  # [Estimat for antall km kjørt for begge bilene, km/år]
forsikring_el = 5000  # [Forsikring for elbil, kr/år]
forsikring_b = 7500  # [Forsikring for bensinbil, kr/år]
trafikkforsikring = 8.38  # [Trafikkforsikring avgift for begge biler kr/dag] 
drivstoff_el = 0.2  # [Drivstoffkostnad for elbil i kWh/km]
drivstoff_b = 1.0   # [Drivstoffkostnader for bensinbil, i kr/km]
strøm = 2.00  # [Strømpris for hjemmelading av elbil kr/kWh]
bomavgift_el = 0.1  # [Bomavgift for elbil, kr/km]
bomavgift_b = 0.3  # [Bomavgift for bensinbil, kr/km]


# In[14]:


trafikkforsikring_år = trafikkforsikring * 365  # [Trafikkforsikringavgift for begge biler kr/år]


# In[15]:


print ("Trafikkforsikrigavgift per år", trafikkforsikring_år)


# In[16]:


drivstoff_forbruk_el_år = km_p_år * drivstoff_el * strøm  # [Drivstoff forbruk for elbil per år, kr/år


# In[17]:


drivstoff_forbruk_b_år = km_p_år * drivstoff_b  # [Drivstoff forbruk for bensinbil per år, kr/år]


# In[18]:


totalkostnad_el = forsikring_el + trafikkforsikring_år + drivstoff_forbruk_el_år + (km_p_år * bomavgift_el) # [Totalkostander for eie av elbil, kr/år]


# In[19]:


totalkostnad_b = forsikring_b + trafikkforsikring_år + drivstoff_forbruk_b_år + (km_p_år * bomavgift_b)  # [Totalkostander for eie av bensinbil, kr/år]


# In[22]:


print ("Totalkostnader for elbil", totalkostnad_el, "kr/år" " og totalkostader for bensinbil", totalkostnad_b, "kr/år")


# In[23]:


differanse = totalkostnad_b - totalkostnad_el


# In[122]:


print ("Differanse mellom å eie en bensinbil og elbil er", Diff, "kr/år")

