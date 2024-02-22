from flask import Blueprint, render_template
from API.api import GetAllProducts, GetSingleProducts
products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    l = len(data)
    


    return render_template('products/products.html', length = l, products = data)

@products_bp.route('/products/<int:id>')
def detailOfProduct(id):
    data = GetSingleProducts(id)

    dataS = GetAllProducts()

    wantedData = []

    a = 0

    for item in dataS:
        if (item['category'] == "women's clothing" and a < 4):
            wantedData.append[item]
            a += 1

    wantedLen = len(wantedData)

    print(wantedLen)
    print(wantedData)


    return render_template('products/detail.html', detailOfPorduct = data, wantedLen = wantedLen, wantedData = wantedData)
