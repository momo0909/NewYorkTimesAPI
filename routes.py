from flask import render_template, request

from Project2_Flask import app, forms, api_methods


@app.route('/')
@app.route('/home')
def index():  ###route for index
    return render_template("index.html")


@app.route('/topArticles.html', methods=["GET", "POST"])
def topArticles():
    my_form = forms.articleForms(request.form)

    if request.method == "POST":
        selected_section = request.form["section"]

        getStories = api_methods.request_newly_api(selected_section)

        lst_art=[10]

        for i in getStories["results"]:


                title = (i["title"],i["published_date"])

                lst_art.append(title)



        return render_template("topArticles_result.html", response=lst_art)
    return render_template("topArticles.html", form=my_form)

@app.route('/bestSellers.html', methods=["GET", "POST"])
def bestSellers():
    book_form = forms.articleForms(request.form)

    if request.method == "POST":
        best_Seller = request.form["genre"]

        get_BestS = api_methods.best_Sellers(best_Seller)

        list_book = [10]

        for i in get_BestS["results"]["books"]:
            b_Title = (i["title"],i["author"])
            list_book.append(b_Title)

        return render_template("bestSellers_result.html", response=list_book)
    return render_template("bestSellers.html", form=book_form)



