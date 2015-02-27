''' This file is used when setting up the database for the first time or
 resetting data to the default sample data '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Company, Base, SalesItem


def load_default_data(session):
    ''' This loads in all the default data given an sqlalchemy
    session as an argument '''

    company_1 = Company(
        name="Shirt.Woot", siteuri="http://shirt.woot.com/")
    session.add(company_1)

    sales_item_0 = SalesItem(
        name="The Binge",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/3b9e7d98-0758-478e-95d"
                  "c-cf335a809af7.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_0)

    sales_item_1 = SalesItem(
        name="The Epic Begins",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/00eb2b1c-838f-45c5-a05"
                  "6-550aff5a1f8e.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_1)

    sales_item_2 = SalesItem(
        name="Family Breakfast",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/d3d970f2-bef5-4b8d-897"
                  "1-cf203b43fe23.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_2)

    sales_item_3 = SalesItem(
        name="Unstealthiest Ninja",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/59dc2972-0a6f-4902-a65"
                  "f-034fecdccf0d.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_3)

    sales_item_4 = SalesItem(
        name="Consider Yourself Warned",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/77dac9c5-6d53-4a48-abf"
                  "5-0cdd70a65aa2.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_4)

    sales_item_5 = SalesItem(
        name="Vincent Van Groot",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/a5c5319d-9d5d-4e31-a28"
                  "c-9b3d998afdeb.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_5)

    sales_item_6 = SalesItem(
        name="Go Sports!",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/7d6eff23-6f72-4b44-b5d"
                  "2-add28da4d2b9.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_6)

    sales_item_7 = SalesItem(
        name="Delete, You Fools",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/fd58820f-c705-4e36-972"
                  "2-5a8d294f13e3.jpg"),
        price="$15.00", company=company_1)
    session.add(sales_item_7)

    sales_item_8 = SalesItem(
        name="MARVELous Clubhouse",
        imageuri=("http://d3gqasl9vmjfd8.cloudfront.net/967c9899-4360-47b1-bae"
                  "b-bb6d137febb0.png"),
        price="$15.00", company=company_1)
    session.add(sales_item_8)

    company_2 = Company(
        name="Threadless", siteuri="https://www.threadless.com/")
    session.add(company_2)

    sales_item_1 = SalesItem(
        name="The Communist Party",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/383/636x460de"
                  "sign_01.jpg"),
        price="$25.00", company=company_2)
    session.add(sales_item_1)

    sales_item_2 = SalesItem(
        name="Funkalicious",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/576/636x460de"
                  "sign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_2)

    sales_item_3 = SalesItem(
        name="Flowers In The Attic",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/114/636x460de"
                  "sign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_3)

    sales_item_4 = SalesItem(
        name="Infinity MPG",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/562/636x460de"
                  "sign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_4)

    sales_item_5 = SalesItem(
        name="Cookie Loves Milk",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/342/636x460de"
                  "sign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_5)

    sales_item_6 = SalesItem(
        name="Running Rhino",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/1000/636x460d"
                  "esign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_6)

    sales_item_7 = SalesItem(
        name="Mister Mitten\'s Big Adventure",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/1354/636x460d"
                  "esign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_7)

    sales_item_8 = SalesItem(
        name="Pandamonium",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/178/636x460de"
                  "sign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_8)

    sales_item_9 = SalesItem(
        name="Bird Of A Feather",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/1160/636x460d"
                  "esign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_9)

    sales_item_10 = SalesItem(
        name="The Horde",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/2059/636x460d"
                  "esign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_10)

    sales_item_11 = SalesItem(
        name="Loch Ness Imposter",
        imageuri=("https://dov5cor25da49.cloudfront.net/products/281/636x460de"
                  "sign_01.jpg"),
        price="$25", company=company_2)
    session.add(sales_item_11)

    company_1 = Company(
        name="Teefury", siteuri="http://www.teefury.com/")
    session.add(company_1)

    sales_item_1 = SalesItem(
        name="Siren",
        imageuri=("http://www.teefury.com/media/catalog/product/cache/1/image/"
                  "800x/17f82f742ffe127f42dca9de82fb58b1/b/-/b-mco-siren.png"),
        price="$20", company=company_1)
    session.add(sales_item_1)

    sales_item_2 = SalesItem(
        name="I Am Not Your Mummy",
        imageuri=("http://www.teefury.com/media/catalog/product/cache/1/produc"
                  "t_artwork_image/900x/17f82f742ffe127f42dca9de82fb58b1/b/-/b"
                  "-mco-i-am-not-your-mummy_blk.jpg"),
        price="$20", company=company_1)
    session.add(sales_item_2)

    sales_item_3 = SalesItem(
        name="Sorry I\'m Not Made of Sugar",
        imageuri=("http://www.teefury.com/media/catalog/product/cache/1/image/"
                  "800x/17f82f742ffe127f42dca9de82fb58b1/b/-/b-mco-sorry-i_m-n"
                  "ot-made-of-sugar.png"),
        price="$20", company=company_1)
    session.add(sales_item_3)

    sales_item_4 = SalesItem(
        name="Snow Wars",
        imageuri=("http://www.teefury.com/media/catalog/product/cache/1/image/"
                  "800x/17f82f742ffe127f42dca9de82fb58b1/b/-/b-mco-snow-wars.p"
                  "ng"),
        price="$20", company=company_1)
    session.add(sales_item_4)

    sales_item_5 = SalesItem(
        name="The Merc with a Mouth",
        imageuri=("http://www.teefury.com/media/catalog/product/cache/1/image/"
                  "800x/17f82f742ffe127f42dca9de82fb58b1/b/-/b-mco-the-merc-wi"
                  "th-the-mouth.png"),
        price="$20", company=company_1)
    session.add(sales_item_5)

    sales_item_6 = SalesItem(
        name="I\'ll Always Protect You",
        imageuri=("http://www.teefury.com/media/catalog/product/cache/1/image/"
                  "800x/17f82f742ffe127f42dca9de82fb58b1/b/-/b-mco-i_ll-always"
                  "-protect-you_2.png"),
        price="$20", company=company_1)
    session.add(sales_item_6)

    company_1 = Company(
        name="6 Dollar Shirts", siteuri="http://www.6dollarshirts.com/t-shirts"
        "/")
    session.add(company_1)

    sales_item_1 = SalesItem(
        name="Nerd Cat",
        imageuri=("http://6dollar.threadpitinc.netdna-cdn.com/images/D/Nerd_Ca"
                  "t_T_SHIRT_detail.jpg"),
        price="$6", company=company_1)
    session.add(sales_item_1)

    sales_item_2 = SalesItem(
        name="Gas Mousk",
        imageuri=("http://6dollar.threadpitinc.netdna-cdn.com/images/D/Gas_Mou"
                  "sk_T_SHIRT_detail.jpg"),
        price="$6", company=company_1)
    session.add(sales_item_2)

    sales_item_3 = SalesItem(
        name="Beer?",
        imageuri=("http://6dollar.threadpitinc.netdna-cdn.com/images/D/Beer_T_"
                  "SHIRT_detail.jpg"),
        price="$6", company=company_1)
    session.add(sales_item_3)

    sales_item_4 = SalesItem(
        name="Pug Life",
        imageuri=("http://6dollar.threadpitinc.netdna-cdn.com/images/D/Pug_Lif"
                  "e_T_SHIRT_detail.jpg"),
        price="$6", company=company_1)
    session.add(sales_item_4)

    sales_item_5 = SalesItem(
        name="Evolution to Termination",
        imageuri=("http://6dollar.threadpitinc.netdna-cdn.com/images/D/Evoluti"
                  "on_Termination_T_SHIRT_detail.jpg"),
        price="$6", company=company_1)
    session.add(sales_item_5)

    sales_item_2 = SalesItem(
        name="I Mustache You A Question",
        imageuri=("http://6dollar.threadpitinc.netdna-cdn.com/images/D/Mustach"
                  "e_Question_T_SHIRT_detail.jpg"),
        price="$6", company=company_1)
    session.add(sales_item_2)

    company_1 = Company(
        name="Busted Tees", siteuri="http://www.bustedtees.com/")
    session.add(company_1)

    sales_item_1 = SalesItem(
        name="Song of Storms",
        imageuri=("http://4.media.bustedtees.cvcdn.com/7/-/bustedtees.3cab35c7"
                  "-9e1e-4316-91a0-78c5f56d.gif"),
        price="$20", company=company_1)
    session.add(sales_item_1)

    sales_item_2 = SalesItem(
        name="Who\'s This",
        imageuri=("http://7.media.bustedtees.cvcdn.com/4/-/bustedtees.0ba45044"
                  "-372e-47c9-918d-d6f9c055.gif"),
        price="$20", company=company_1)
    session.add(sales_item_2)

    sales_item_3 = SalesItem(
        name="Control Freak",
        imageuri=("http://2.media.bustedtees.cvcdn.com/3/-/bustedtees.9882d363"
                  "-49ad-48a1-b23a-fb254726.gif"),
        price="$20", company=company_1)
    session.add(sales_item_3)

    sales_item_4 = SalesItem(
        name="Boo vs. Angel",
        imageuri=("http://1.media.bustedtees.cvcdn.com/e/-/bustedtees.2b16debe"
                  "-dcec-435d-9418-c9988245968f.gif"),
        price="$12", company=company_1)
    session.add(sales_item_4)

    sales_item_5 = SalesItem(
        name="Haters Gonna Hate",
        imageuri=("http://4.media.bustedtees.cvcdn.com/c/-/bustedtees.144ff9bc"
                  "-01d6-4301-8df6-ca61ceb8.gif"),
        price="$20", company=company_1)
    session.add(sales_item_5)

    # commit all of that at once
    session.commit()


if __name__ == '__main__':
    engine = create_engine('sqlite:///catalog.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    this_session = DBSession()
    load_default_data(this_session)
    print "added sales items!"
