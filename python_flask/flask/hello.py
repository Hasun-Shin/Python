from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/hi')
def hi():
    name = "신하선"
    return render_template('hi.html',html_name =name)
    

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)


@app.route('/cube/<int:num>')
def cube(num):
    
    cube_num = num**3
    return render_template('cube.html',cube_num = cube_num, num = num)


@app.route('/fstring')
def fstring():
    fstring = "신하선"
    return f"제 이름은 {fstring} 입니다."


@app.route('/dinner')
def dinner():
    menu = ['삼각김밥','컵라면','스테이크','마라탕','훠궈']
    dinner = random.choice(menu)
    menu_img = {'삼각김밥': 'https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwiyl5fDiMHmAhXGMt4KHXjiDdUQjRx6BAgBEAQ&url=http%3A%2F%2Femart.ssg.com%2Fitem%2FitemView.ssg%3FitemId%3D1000024971696%26siteNo%3D6001%26salestrNo%3D2034&psig=AOvVaw1lomw97UbO4n-C--L_XITT&ust=1576822715983193',
                '컵라면': 'https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwivusjUiMHmAhXDa94KHSB7AuwQjRx6BAgBEAQ&url=http%3A%2F%2Fitempage3.auction.co.kr%2FDetailView.aspx%3Fitemno%3DA871315661&psig=AOvVaw1pxnQPfbWg1VgwdbKQTwth&ust=1576822756178256',
                '스테이크': 'https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjl1JHfiMHmAhUafnAKHf7UD8IQjRx6BAgBEAQ&url=https%3A%2F%2Fmannabox.co.kr%2Fmanna%2Fview%3Fno%3D300&psig=AOvVaw1eG-7abxH6JiYMb9q_GyiA&ust=1576822776386059',
                '마라탕': 'https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/4BYf/image/_pc0k6Jz3BHHLVwylaQYEPZdQd0.jfif',
                '훠궈': 'https://post-phinf.pstatic.net/MjAxNzExMzBfMTg2/MDAxNTEyMDEyNDE3OTI1.W1uSSVqYNq9NS8tHODn59RIyXo5-7zByKdSwqCZlN2Qg.4CdNKyPOen6sUSYXF_DW3h_fICYAnlfncEB2B6Y3vnAg.JPEG/%ED%9B%A0%EA%B6%88%EC%95%BC_MangoPlate_%EC%98%A4%EC%A7%80%EC%88%99.jpg?type=w1200'}
    
    
    img_url = menu_img[dinner]
    return render_template('dinner.html', dinner = dinner, img_url = img_url)


@app.route('/movies')
def movies():
    movies = ['조커','겨울왕국2','터미네이터','어벤져스']
    return render_template('movies.html', movies = movies)





if __name__ == "__main__":
    app.run(debug=True)


