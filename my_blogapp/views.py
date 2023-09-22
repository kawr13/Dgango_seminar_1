from django.shortcuts import render, HttpResponse
import logging



logger = logging.getLogger(__name__)



def index(request):
    return HttpResponse(
        '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная страница</title>
    <!-- Подключение стилей Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Мой Вебсайт</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Главная <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/about/">Обо мне</a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container mt-5">
        <h1>Добро пожаловать на главную страницу</h1>
    </div>

    <!-- Подключение скриптов Bootstrap (jQuery и Popper.js) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
'''
    )


def about(request):
    return HttpResponse(
        '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
    <!-- Подключение стилей Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Мой Вебсайт</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/">Главная</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="#">Обо мне <span class="sr-only">(current)</span></a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container mt-5">
        <h1>Обо мне</h1>
        <p>Я начинающий программист, страстно увлеченный миром кодирования и разработки. Мои первые шаги в программировании были заполнены увлекательными открытиями и решением разнообразных задач. Я постоянно учусь и стремлюсь к совершенствованию своих навыков, и каждый новый проект становится для меня возможностью расти и развиваться в этой увлекательной области. В моем арсенале уже есть базовые знания Python, и я готов исследовать более глубокие аспекты программирования, чтобы внести свой вклад в мир технологий.</p>
        <a href="/">Вернуться на главную</a>
    </div>

    <!-- Подключение скриптов Bootstrap (jQuery и Popper.js) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
'''
    )


def blog(request):
    return HttpResponse(
        '''<!DOCTYPE html>
            <html data-bs-theme="light" lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
                <title>Home - Brand</title>
                <link rel="stylesheet" href="/static/assets/bootstrap/css/bootstrap.min.css?h=cb8828c28cbb36ccaba2a87636c9f589">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <link rel="stylesheet" href="/static/assets/css/styles.min.css?h=536e62e6d7a1a104c741b5e807552c44">
            </head>
            <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="72">
            <nav class="navbar navbar-expand-lg fixed-top bg-secondary text-uppercase navbar-light" id="mainNav">
                <div class="container"><a class="navbar-brand" href="#page-top">Мой блог</a>
                    <button data-bs-toggle="collapse" data-bs-target="#navbarResponsive"
                            class="navbar-toggler text-white bg-primary navbar-toggler-right text-uppercase rounded"
                            aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><i
                            class="fa fa-bars"></i></button>
                    <div class="collapse navbar-collapse" id="navbarResponsive">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item mx-0 mx-lg-1"></li>
                            <li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded" href="#about">About</a>
                            </li>
                            <li class="nav-item mx-0 mx-lg-1"><a class="nav-link py-3 px-0 px-lg-3 rounded"
                                                                 href="#contact">Contact</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <header class="text-center text-white bg-primary masthead">
                <div class="container"><img class="img-fluid d-block mx-auto mb-5"
                                            src="/static/assets/img/profile.png?h=ca1ddcee1cb057489d44a94e63b7fbc4">
                    <h1>Alex</h1>
                    <hr class="star-light">
                    <h2 class="font-weight-light mb-0">Начинающий программист, дизайнер, фотограф, видеограф</h2></div>
            </header>
            <section class="text-white bg-primary mb-0" id="about">
                <div class="container"><h2 class="text-uppercase text-center text-white">Обомне</h2>
                    <hr class="star-light mb-5">
                    <div class="row">
                        <div class="col-lg-4 ms-auto"><p class="lead text-start">Я начинающий программист, страстно увлеченный миром
                            кодирования и разработки. Мои первые шаги в программировании были заполнены увлекательными открытиями и
                            решением разнообразных задач. Я постоянно <br>учусь и стремлюсь к совершенствованию своих<br><br></p>
                        </div>
                        <div class="col-lg-4 me-auto"><p class="lead">&nbsp;навыков, и каждый новый проект становится для меня
                            возможностью расти и развиваться в этой увлекательной области. В моем арсенале уже есть базовые знания
                            Python, и я готов исследовать более глубокие аспекты программирования, чтобы внести свой вклад в мир
                            технологий.<br><br></p></div>
                    </div>
                    <div class="text-center mt-4"></div>
                </div>
            </section>
            <section id="contact">
                <div class="container"><h2 class="text-uppercase text-center text-secondary mb-0">Свяжись со мной</h2>
                    <hr class="star-dark mb-5">
                    <div class="row">
                        <div class="col-lg-8 mx-auto">
                            <form id="contactForm" name="sentMessage">
                                <div class="control-group">
                                    <div class="mb-0 form-floating controls pb-2"><input class="form-control" type="text" id="name"
                                                                                         required="" placeholder="Name"><label
                                            class="form-label">Name</label><small class="form-text text-danger help-block"></small>
                                    </div>
                                </div>
                                <div class="control-group">
                                    <div class="mb-0 form-floating controls pb-2"><input class="form-control" type="email"
                                                                                         id="email" required=""
                                                                                         placeholder="Email Address"><label
                                            class="form-label">Email Address</label><small
                                            class="form-text text-danger help-block"></small></div>
                                </div>
                                <div class="control-group">
                                    <div class="mb-0 form-floating controls pb-2"><input class="form-control" type="tel" id="phone"
                                                                                         required=""
                                                                                         placeholder="Phone Number"><label
                                            class="form-label">Phone Number</label><small
                                            class="form-text text-danger help-block"></small></div>
                                </div>
                                <div class="control-group">
                                    <div class="mb-5 form-floating controls pb-2"><textarea class="form-control" id="message"
                                                                                            required="" placeholder="Message"
                                                                                            style="height: 150px;"></textarea><label
                                            class="form-label">Message</label><small
                                            class="form-text text-danger help-block"></small></div>
                                </div>
                                <div id="success"></div>
                                <div>
                                    <button class="btn btn-primary btn-xl" id="sendMessageButton" type="submit">Send</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </section>
            <footer class="text-center footer">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4 mb-5 mb-lg-0"><h4 class="text-uppercase mb-4">адрес</h4>
                            <p>2215 John Daniel Drive<br>Clark, MO 65243</p></div>
                        <div class="col-md-4 mb-5 mb-lg-0"><h4 class="text-uppercase">Around the Web</h4>
                            <ul class="list-inline">
                                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle"
                                                                role="button" href="#"><i class="fa fa-facebook fa-fw"></i></a></li>
                                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle"
                                                                role="button" href="#"><i class="fa fa-google-plus fa-fw"></i></a>
                                </li>
                                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle"
                                                                role="button" href="#"><i class="fa fa-twitter fa-fw"></i></a></li>
                                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle"
                                                                role="button" href="#"><i class="fa fa-dribbble fa-fw"></i></a></li>
                            </ul>
                        </div>
                        <div class="col-md-4"><p class="lead mb-0"></p></div>
                    </div>
                </div>
            </footer>
            <div class="text-center text-white copyright py-4">
                <div class="container"><small>Copyright ©&nbsp;Brand 2023</small></div>
            </div>
            <div class="d-lg-none scroll-to-top position-fixed rounded"><a class="text-center d-block rounded text-white"
                                                                           href="#page-top"><i class="fa fa-chevron-up"></i></a>
            </div>
            <div class="modal text-center" role="dialog" tabindex="-1" id="portfolio-modal-1">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col-lg-8 mx-auto"><h2 class="text-uppercase text-secondary mb-0">Project Name</h2>
                                        <hr class="star-dark mb-5">
                                        <img class="img-fluid mb-5"
                                             src="/static/assets/img/portfolio/cabin.png?h=5bde47039f23de84a7748bee08793ac3">
                                        <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                            assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit
                                            asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p></div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer pb-5"><a
                                class="btn btn-primary btn-lg mx-auto rounded-pill portfolio-modal-dismiss" role="button"
                                data-bs-dismiss="modal"><i class="fa fa-close"></i>&nbsp;Close Project</a></div>
                    </div>
                </div>
            </div>
            <div class="modal text-center" role="dialog" tabindex="-1" id="portfolio-modal-2">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col-lg-8 mx-auto"><h2 class="text-uppercase text-secondary mb-0">Project Name</h2>
                                        <hr class="star-dark mb-5">
                                        <img class="img-fluid mb-5"
                                             src="/static/assets/img/portfolio/cake.png?h=4b5723e2b00006ef3a25df097c7187dd">
                                        <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                            assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit
                                            asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p></div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer pb-5"><a
                                class="btn btn-primary btn-lg mx-auto rounded-pill portfolio-modal-dismiss" role="button"
                                data-bs-dismiss="modal"><i class="fa fa-close"></i>&nbsp;Close Project</a></div>
                    </div>
                </div>
            </div>
            <div class="modal text-center" role="dialog" tabindex="-1" id="portfolio-modal-3">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col-lg-8 mx-auto"><h2 class="text-uppercase text-secondary mb-0">Project Name</h2>
                                        <hr class="star-dark mb-5">
                                        <img class="img-fluid mb-5"
                                             src="/static/assets/img/portfolio/circus.png?h=984b4ff719255fcbf2e01164905ebb90">
                                        <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                            assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit
                                            asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p></div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer pb-5"><a
                                class="btn btn-primary btn-lg mx-auto rounded-pill portfolio-modal-dismiss" role="button"
                                data-bs-dismiss="modal"><i class="fa fa-close"></i>&nbsp;Close Project</a></div>
                    </div>
                </div>
            </div>
            <div class="modal text-center" role="dialog" tabindex="-1" id="portfolio-modal-4">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col-lg-8 mx-auto"><h2 class="text-uppercase text-secondary mb-0">Project Name</h2>
                                        <hr class="star-dark mb-5">
                                        <img class="img-fluid mb-5"
                                             src="/static/assets/img/portfolio/game.png?h=b5df08ec517f8b9872be52e015333d8a">
                                        <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                            assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit
                                            asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p></div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer pb-5"><a
                                class="btn btn-primary btn-lg mx-auto rounded-pill portfolio-modal-dismiss" role="button"
                                data-bs-dismiss="modal"><i class="fa fa-close"></i>&nbsp;Close Project</a></div>
                    </div>
                </div>
            </div>
            <div class="modal text-center" role="dialog" tabindex="-1" id="portfolio-modal-5">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col-lg-8 mx-auto"><h2 class="text-uppercase text-secondary mb-0">Project Name</h2>
                                        <hr class="star-dark mb-5">
                                        <img class="img-fluid mb-5"
                                             src="/static/assets/img/portfolio/safe.png?h=77cbc82936acf11b03bd687ff795e835">
                                        <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                            assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit
                                            asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p></div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer pb-5"><a
                                class="btn btn-primary btn-lg mx-auto rounded-pill portfolio-modal-dismiss" role="button"
                                data-bs-dismiss="modal"><i class="fa fa-close"></i>&nbsp;Close Project</a></div>
                    </div>
                </div>
            </div>
            <div class="modal text-center" role="dialog" tabindex="-1" id="portfolio-modal-6">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button class="btn-close" type="button" aria-label="Close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col-lg-8 mx-auto"><h2 class="text-uppercase text-secondary mb-0">Project Name</h2>
                                        <hr class="star-dark mb-5">
                                        <img class="img-fluid mb-5"
                                             src="/static/assets/img/portfolio/submarine.png?h=71572e367539ee27f418326f2361bce2">
                                        <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                            assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit
                                            asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p></div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer pb-5"><a
                                class="btn btn-primary btn-lg mx-auto rounded-pill portfolio-modal-dismiss" role="button"
                                data-bs-dismiss="modal"><i class="fa fa-close"></i>&nbsp;Close Project</a></div>
                    </div>
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
            <script src="/static/assets/js/script.min.js?h=33588ed143bc098cbcf279ea5d7aa7b8"></script>
            </body>
    </html>'''
    )
