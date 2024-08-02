import base64

encoded = base64.b64encode(open("arrow.png", "rb").read()).decode()

def create_html_page(news_list):
    page = """
<html>
    <style>
        .page {
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            background-color: #e6f0dc;
            border-radius: 10px;
            width: 70%;
            min-width: 600px;
            margin: auto;
        }

        .header {
            background-color: #55883b;
            margin: auto;
            text-align: center;
            height: 70;
            padding: 5;
            border-radius: 10px;
            border-bottom-left-radius: 0;
            border-bottom-right-radius: 0;
        }

        .card-wrapper {
            padding: 20;
        }

        .card {
            display: flex;
            background-color: #c1e899;
            border-radius: 10px;
            width: 90%;
            margin: auto;
            padding: 20px;
        }

        .text {
            flex: 0 0 80%;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
        }
        
        .linkbutton {
            flex: 0 0 20%;
            text-align: center;
            margin: auto;
        }

        a {
            text-decoration: none;
            margin: auto;
        }

        img {
            width: 50px;
        }
    </style>
    
    <div class="page">
        <div class="header">
            <h1>Your Morning Feed</h1>
        </div>
        <div class="card-wrapper">
    """

    articles_list = ""

    for article in news_list[:10]:
        article_html = """
            <div class="card" style="display: flex;">

                <div class="text">
                    <p> 
                    %s
                    </p>
                </div>
                <div class="linkbutton">
                    <a href="%s">""" % (article["title"], article["link"])
                
        
        img_part = f"""
                <img src="data:image/png;base64,{encoded}"> </a>
                </div>
                </div>
                <br>
            """ 
        total = article_html + img_part
        articles_list += total

    page += articles_list

    page += """</div>
                <br>
            </div>
            
        </html>"""
    
    return page