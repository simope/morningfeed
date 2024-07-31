import base64

encoded = base64.b64encode(open("arrow.png", "rb").read()).decode()

def create_html_page(news_list):
    page = """
<html>
    <style>
        .page {
            font-family:  "Courier New";
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
        }

        .linkbutton {
            flex: 0 0 20%;
            font-size: 40;
            margin: auto;
        }

        .text {
            flex: 0 0 80%;
            padding: 20;
            width: 70%;
        }

        a {
            text-decoration: none;
        }

        img {
            width: 25%
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