# NovStore
My first online store

# 📫 How to reach me Telegram: @rayqvaza

# About The Project
Django project, forked and edited (http://djangogreatkart.com/). Added favourite tab & functionality, changed name. 
 In this project i've improved my skills in html, css, django and python.

 </n>Before (main page)/ До моих изменений (главная страница)
![before](https://github.com/BogdanNovokshonov/NovStore/assets/120629135/3774214b-7405-4f03-8268-c1a9e775bc43)


After (main page)/ После моих изменений (главная страница)
![After](https://github.com/BogdanNovokshonov/NovStore/assets/120629135/bed8e327-62b9-49ad-8efb-653352aafdb0)


This is how cart looks like/ Вот так выглядит корзина
![Cart](https://github.com/BogdanNovokshonov/NovStore/assets/120629135/fecb588a-3d73-43dc-af08-01207280bc92)


This is how "favourite" tab looks like. As you can see it is completely different from the shopping cart in both quantity and appearance/ Вот так выглядит вкладка "понравившиеся". 
Как видите она полностью отличается от корзины и по количеству и по своему виду 
![Favourite](https://github.com/BogdanNovokshonov/NovStore/assets/120629135/4de4da2a-9ec6-429b-aca8-647916210a16)


Page with product details before/Страница с деталями продукта до изменений
![prod details before](https://github.com/BogdanNovokshonov/NovStore/assets/120629135/01659848-8235-43c3-9a5d-5413bbe45ee9)


After/После 
![Product details after](https://github.com/BogdanNovokshonov/NovStore/assets/120629135/b9c5a4b1-7c7e-4b48-9166-b1dbab7c2f68)




# Setup Instructions

1. Clone the repository `git clone https://github.com/BogdanNovokshonov/NovStore`
2. Navigrate to the working directory `cd greatkart-pre-deploy`
3. Open the project from the code editor `code .` or `atom .`
4. Create virtual environment `python -m venv env`
5. Activate the virtual environment `source env/Scripts/activate`
6. Install required packages to run the project `pip install -r requirements.txt`
7. Rename _.env-sample_ to _.env_
8. Fill up the environment variables:
    _Generate your own Secret key using this tool [https://djecrety.ir/](https://djecrety.ir/), copy and paste the secret key in the SECRET_KEY field._

    _Your configuration should look something like this:_
    ```sh
    SECRET_KEY=47d)n05#ei0rg4#)*@fuhc%$5+0n(t%jgxg$)!1pkegsi*l4c%
    DEBUG=True
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=youremailaddress@gmail.com
    EMAIL_HOST_PASSWORD=yourStrongPassword
    EMAIL_USE_TLS=True
    ```
    _Note: If you are using gmail account, make sure to [use app password](https://support.google.com/accounts/answer/185833)_
9. Create database tables
    ```sh
    python manage.py migrate
    ```
10. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
11. Run server
    ```sh
    python manage.py runserver
    ```
12. Login to admin panel - (`http://127.0.0.1:8000/securelogin/`)
13. Add categories, products, add variations, register user, login, place orders and EXPLORE SO MANY FEATURES




## Support
💙 If you like this project, give it a ⭐ and share it with friends!

<p align="left">
  📫 **How to reach me** Telegram: @rayqvaza
</p>

## Contact Me
<p align="left">
  📫 **How to reach me** Telegram: @rayqvaza
</p>

##
Made with ❤️ and Python
