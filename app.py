from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home-creative-blog')
def home_creative_blog():
    return render_template('home-creative-blog.html')

@app.route('/home-lifestyle-blog')
def home_lifestyle_blog():
    return render_template('home-lifestyle-blog.html')

@app.route('/home-seo-blog')
def home_seo_blog():
    return render_template('home-seo-blog.html')

@app.route('/home-tech-blog')
def home_tech_blog():
    return render_template('home-tech-blog.html')

@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')

@app.route('/post-details')
def post_details():
    return render_template('post-details.html')

@app.route('/post-format-gallery')
def post_format_gallery():
    return render_template('post-format-gallery.html')

@app.route('/post-format-standard')
def post_format_standard():
    return render_template('post-format-standard.html')

@app.route('/post-format-text')
def post_format_text():
    return render_template('post-format-text.html')

@app.route('/post-format-video')
def post_format_video():
    return render_template('post-format-video.html')

@app.route('/post-layout-1')
def post_layout_1():
    return render_template('post-layout-1.html')

@app.route('/post-list')
def post_list():
    return render_template('post-list.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

# Gestion de la page 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)