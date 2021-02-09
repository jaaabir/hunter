                                 _     _ _     _ __   _ _______ _______  ______
                                 |_____| |     | | \  |    |    |______ |_____/
                                 |     | |_____| |  \_|    |    |______ |    \_


---

**_Simple email hunter using hunter's api_**
---


# Documentation 
<br>

[hunter api documentation](https://hunter.io/api-documentation/v2)

---

# Usage 
<br>

* **Get API Key from** [hunter.io](https://hunter.io/api-keys)
* **After getting the API Key , save it in the settings.ini file**

---

#### [options]

<br>

[0](https://hunter.io/api-documentation/v2#domain-search) - search by domain (domain search) <br>
[1](https://hunter.io/api-documentation/v2#email-finder) - gets the info for the specified person (email finder) <br>
[2](https://hunter.io/api-documentation/v2#email-verifier) - gets the info for the specified email (email verifier) <br>
[3](https://hunter.io/api-documentation/v2#email-count) - gets the number of emails in the specified domain (email counter) Saves the output to a file <br>
<br>
**use --output or -o to save the result in a csv file** 
<br>

---


### Windows 
<br>
python hunter.py -s [option] <br>
python hunter.py -s [option] --output 

<br>

---

### mac/linux
<br>
python3 hunter.py -s [option] <br>
python3 hunter.py -s [option] --output




