<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11 WebFlux 实战图书管理系统.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="01&#32;导读：课程概要.md">01 导读：课程概要.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;WebFlux&#32;快速入门实践.md">02 WebFlux 快速入门实践.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;WebFlux&#32;Web&#32;CRUD&#32;实践.md">03 WebFlux Web CRUD 实践.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;WebFlux&#32;整合&#32;MongoDB.md">04 WebFlux 整合 MongoDB.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;WebFlux&#32;整合&#32;Thymeleaf.md">05 WebFlux 整合 Thymeleaf.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;WebFlux&#32;中&#32;Thymeleaf&#32;和&#32;MongoDB&#32;实践.md">06 WebFlux 中 Thymeleaf 和 MongoDB 实践.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;WebFlux&#32;整合&#32;Redis.md">07 WebFlux 整合 Redis.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;WebFlux&#32;中&#32;Redis&#32;实现缓存.md">08 WebFlux 中 Redis 实现缓存.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;WebFlux&#32;中&#32;WebSocket&#32;实现通信.md">09 WebFlux 中 WebSocket 实现通信.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;WebFlux&#32;集成测试及部署.md">10 WebFlux 集成测试及部署.md</a>

                </li>
                <li>

                    <a class="current-tab" href="11&#32;WebFlux&#32;实战图书管理系统.md">11 WebFlux 实战图书管理系统.md</a>
                    

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>11 WebFlux 实战图书管理系统</h1>
<h3>前言</h3>
<p>本篇内容我们会实现如下图所示的城市管理系统，因为上面案例都用的是 City，所以这里直接使用城市作为对象，写一个简单的城市管理系统，如图所示：</p>
<p><img src="assets/99e91edf11b6ff64025c7a74c4a1db561525504.png" alt="file" /></p>
<h3>结构</h3>
<p>类似上面讲的工程搭建，新建一个工程编写此案例。工程如图：</p>
<p><img src="assets/1a05190038e9565a3ffa1b876a63f4701525504.png" alt="img" /></p>
<p>下面目录和上面类似，这边不重复讲解：</p>
<ul>
<li>pom.xml Maven 依赖配置</li>
<li>application.properties 配置文件，配置 mongo 连接属性配置</li>
<li>dao 数据访问层</li>
</ul>
<p><a href="https://github.com/JeffLi1993/springboot-learning-example">单击这里查看源代码</a>。</p>
<p>本文主要介绍：</p>
<ul>
<li>controller 控制层实现</li>
<li>static 存放 css 图片静态资源</li>
<li>templates 编写页面逻辑</li>
</ul>
<h3>CityController 控制层</h3>
<p>使用注解驱动的模式来进行开发，代码如下：</p>
<pre><code>/**
 * city 控制层
 * &lt;p&gt;
 * Created by bysocket
 */
@Controller
@RequestMapping(value = &quot;/city&quot;)
public class CityController {

    private static final String CITY_FORM_PATH_NAME = &quot;cityForm&quot;;
    private static final String CITY_LIST_PATH_NAME = &quot;cityList&quot;;
    private static final String REDIRECT_TO_CITY_URL = &quot;redirect:/city&quot;;

    @Autowired
    CityService cityService;

    @RequestMapping(method = RequestMethod.GET)
    public String getCityList(final Model model) {
        model.addAttribute(&quot;cityList&quot;, cityService.findAll());
        return CITY_LIST_PATH_NAME;
    }

    @RequestMapping(value = &quot;/create&quot;, method = RequestMethod.GET)
    public String createCityForm(final Model model) {
        model.addAttribute(&quot;city&quot;, new City());
        model.addAttribute(&quot;action&quot;, &quot;create&quot;);
        return CITY_FORM_PATH_NAME;
    }

    @RequestMapping(value = &quot;/create&quot;, method = RequestMethod.POST)
    public String postCity(@ModelAttribute City city) {
        cityService.insertByCity(city);
        return REDIRECT_TO_CITY_URL;
    }

    @RequestMapping(value = &quot;/update/{id}&quot;, method = RequestMethod.GET)
    public String getCity(@PathVariable Long id, final Model model) {
        final Mono&lt;City&gt; city = cityService.findById(id);
        model.addAttribute(&quot;city&quot;, city);
        model.addAttribute(&quot;action&quot;, &quot;update&quot;);
        return CITY_FORM_PATH_NAME;
    }

    @RequestMapping(value = &quot;/update&quot;, method = RequestMethod.POST)
    public String putBook(@ModelAttribute City city) {
        cityService.update(city);
        return REDIRECT_TO_CITY_URL;
    }

    @RequestMapping(value = &quot;/delete/{id}&quot;, method = RequestMethod.GET)
    public String deleteCity(@PathVariable Long id) {
        cityService.delete(id);
        return CITY_LIST_PATH_NAME;
    }

}

</code></pre>
<p>可以创建不同功能的控制层，来处理不同的 HTTP 业务请求，比如 CityFrontController、CityAdminController 等分别处理不同场景的问题。</p>
<ul>
<li>getCityList 方法：处理“/city”的 GET 请求，用来获取 City 列表。</li>
<li>getCity 方法：处理“/city/update/{id}”的 GET 请求，用来获取 City 信息。</li>
<li>postCity 方法：处理“/book/create”的 POST 请求，用来新建 Book 信息；通过 @ModelAttribut 绑定实体参数，也通过 @RequestBody @RequestParam 传递参数。</li>
<li>putCity 方法：处理“/update”的 PUT 请求，用来更新 City 信息，并使用 redirect 重定向到列表页面。</li>
</ul>
<h3>cityForm 提交表单页面</h3>
<p>表单页面如下：</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;zh-CN&quot;&gt;
&lt;head&gt;
  &lt;script type=&quot;text/javascript&quot; th:src=&quot;@{https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js}&quot;&gt;&lt;/script&gt;
  &lt;link th:href=&quot;@{https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css}&quot; rel=&quot;stylesheet&quot;/&gt;
  &lt;link th:href=&quot;@{/css/default.css}&quot; rel=&quot;stylesheet&quot;/&gt;
  &lt;link rel=&quot;icon&quot; th:href=&quot;@{/images/favicon.ico}&quot; type=&quot;image/x-icon&quot;/&gt;
  &lt;meta charset=&quot;UTF-8&quot;/&gt;
  &lt;title&gt;城市管理&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;
&lt;div class=&quot;contentDiv&quot;&gt;

  &lt;legend&gt;
    &lt;strong&gt;城市管理&lt;/strong&gt;
  &lt;/legend&gt;

  &lt;form th:action=&quot;@{/city/{action}(action=${action})}&quot; method=&quot;post&quot; class=&quot;form-horizontal&quot;&gt;

    &lt;div class=&quot;form-group&quot;&gt;
      &lt;label for=&quot;city_id&quot; class=&quot;col-sm-2 control-label&quot;&gt;城市编号:&lt;/label&gt;
      &lt;div class=&quot;col-xs-4&quot;&gt;
        &lt;input type=&quot;text&quot; class=&quot;form-control&quot; id=&quot;city_id&quot; name=&quot;id&quot; th:value=&quot;${city.id}&quot;/&gt;
      &lt;/div&gt;
    &lt;/div&gt;

    &lt;div class=&quot;form-group&quot;&gt;
      &lt;label for=&quot;city_name&quot; class=&quot;col-sm-2 control-label&quot;&gt;城市名称:&lt;/label&gt;
      &lt;div class=&quot;col-xs-4&quot;&gt;
        &lt;input type=&quot;text&quot; class=&quot;form-control&quot; id=&quot;city_name&quot; name=&quot;cityName&quot; th:value=&quot;${city.cityName}&quot;/&gt;
      &lt;/div&gt;
    &lt;/div&gt;

    &lt;div class=&quot;form-group&quot;&gt;
      &lt;label for=&quot;city_description&quot; class=&quot;col-sm-2 control-label&quot;&gt;城市描述:&lt;/label&gt;
      &lt;div class=&quot;col-xs-4&quot;&gt;
        &lt;input class=&quot;form-control&quot; id=&quot;city_description&quot; rows=&quot;3&quot; name=&quot;description&quot;
                  th:value=&quot;${city.description}&quot; /&gt;

      &lt;/div&gt;
    &lt;/div&gt;

    &lt;div class=&quot;form-group&quot;&gt;
      &lt;label for=&quot;city_provinceId&quot; class=&quot;col-sm-2 control-label&quot;&gt;省份编号:&lt;/label&gt;
      &lt;div class=&quot;col-xs-4&quot;&gt;
        &lt;input type=&quot;text&quot; class=&quot;form-control&quot; id=&quot;city_provinceId&quot; name=&quot;provinceId&quot; th:value=&quot;${city.provinceId}&quot;
               /&gt;
      &lt;/div&gt;
    &lt;/div&gt;

    &lt;div class=&quot;form-group&quot;&gt;
      &lt;div class=&quot;col-sm-offset-2 col-sm-10&quot;&gt;
        &lt;input class=&quot;btn btn-primary&quot; type=&quot;submit&quot; value=&quot;提交&quot;/&gt;&amp;nbsp;&amp;nbsp;
        &lt;input class=&quot;btn&quot; type=&quot;button&quot; value=&quot;返回&quot; onclick=&quot;history.back()&quot;/&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/form&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

</code></pre>
<p>利用的是 Thymeleaf 语法，上面章节也讲过具体使用方法，这里实现新增城市和更新城市两个操作。巧妙利用了 action 字段去动态判断请求是新增还是更新的控制层方法，然后进行 form 表单提交。</p>
<h3>cityList 城市列表页面</h3>
<p>列表页面代码如下：</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;zh-CN&quot;&gt;
&lt;head&gt;
    &lt;script type=&quot;text/javascript&quot; th:src=&quot;@{https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js}&quot;&gt;&lt;/script&gt;
    &lt;link th:href=&quot;@{https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css}&quot; rel=&quot;stylesheet&quot;/&gt;
    &lt;link th:href=&quot;@{/css/default.css}&quot; rel=&quot;stylesheet&quot;/&gt;
    &lt;link rel=&quot;icon&quot; th:href=&quot;@{/images/favicon.ico}&quot; type=&quot;image/x-icon&quot;/&gt;
    &lt;meta charset=&quot;UTF-8&quot;/&gt;
    &lt;title&gt;城市列表&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;

&lt;div class=&quot;contentDiv&quot;&gt;

    &lt;table class=&quot;table table-hover table-condensed&quot;&gt;
        &lt;legend&gt;
            &lt;strong&gt;城市列表&lt;/strong&gt;
        &lt;/legend&gt;
        &lt;thead&gt;
        &lt;tr&gt;
            &lt;th&gt;城市编号&lt;/th&gt;
            &lt;th&gt;城市名称&lt;/th&gt;
            &lt;th&gt;描述&lt;/th&gt;
            &lt;th&gt;省份编号&lt;/th&gt;
            &lt;th&gt;管理&lt;/th&gt;
        &lt;/tr&gt;
        &lt;/thead&gt;
        &lt;tbody&gt;
        &lt;tr th:each=&quot;city : ${cityList}&quot;&gt;
            &lt;th scope=&quot;row&quot; th:text=&quot;${city.id}&quot;&gt;&lt;/th&gt;
            &lt;td&gt;&lt;a th:href=&quot;@{/city/update/{cityId}(cityId=${city.id})}&quot; th:text=&quot;${city.cityName}&quot;&gt;&lt;/a&gt;&lt;/td&gt;
            &lt;td th:text=&quot;${city.description}&quot;&gt;&lt;/td&gt;
            &lt;td th:text=&quot;${city.provinceId}&quot;&gt;&lt;/td&gt;
            &lt;td&gt;&lt;a class=&quot;btn btn-danger&quot; th:href=&quot;@{/city/delete/{cityId}(cityId=${city.id})}&quot;&gt;删除&lt;/a&gt;&lt;/td&gt;
        &lt;/tr&gt;

        &lt;/tbody&gt;
    &lt;/table&gt;

    &lt;div&gt;&lt;a class=&quot;btn btn-primary&quot; href=&quot;/city/create&quot; role=&quot;button&quot;&gt;新增城市&lt;/a&gt;&lt;/div&gt;
&lt;/div&gt;

&lt;/body&gt;
&lt;/html&gt;

</code></pre>
<p>这里编写了一个列表对象的循环和简单的页面跳转逻辑，下面看看这两个页面组合使用的运行场景。</p>
<h3>运行工程</h3>
<p>一个 CRUD 的 Spring Boot Webflux 工程就开发完毕了，下面运行工程验证一下。使用 IDEA 右侧工具栏，点击 Maven Project Tab 选项，单击使用下 Maven 插件的 install 命令；或者使用命令行的形式，在工程根目录下，执行 Maven 清理和安装工程的指令：</p>
<pre><code>cd springboot-webflux-10-book-manage-sys
mvn clean install

</code></pre>
<p>在控制台中看到成功的输出：</p>
<pre><code>... 省略
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 01:30 min
[INFO] Finished at: 2017-10-15T10:00:54+08:00
[INFO] Final Memory: 31M/174M
[INFO] ------------------------------------------------------------------------

</code></pre>
<p>在 IDEA 中执行 Application 类启动，任意正常模式或者 Debug 模式，可以在控制台看到成功运行的输出：</p>
<pre><code>... 省略
2018-04-10 08:43:39.932  INFO 2052 --- [ctor-http-nio-1] r.ipc.netty.tcp.BlockingNettyContext     : Started HttpServer on /0:0:0:0:0:0:0:0:8080
2018-04-10 08:43:39.935  INFO 2052 --- [           main] o.s.b.web.embedded.netty.NettyWebServer  : Netty started on port(s): 8080
2018-04-10 08:43:39.960  INFO 2052 --- [           main] org.spring.springboot.Application        : Started Application in 6.547 seconds (JVM running for 9.851)

</code></pre>
<p>打开浏览器，输入地址：http://localhost:8080/city，即打开城市列表页面：</p>
<p><img src="assets/99e91edf11b6ff64025c7a74c4a1db561525504-1608971466446.png" alt="file" /></p>
<p>然后新增，或者单击城市名称修改，到表单提交页面：</p>
<p><img src="assets/e9364ebeb39e5a17cb8ee10bdd1736381525505.png" alt="file" /></p>
<h3>总结</h3>
<p>这里，初步实现了小案例城市管理系统，基本满足日常的 CRUD 业务流程操作。上手教程只是上手，具体复杂逻辑，欢迎一起多交流学习。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;WebFlux&#32;集成测试及部署.md">上一页</a>
                        </div>
                        
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355f52fd0645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%A1%88%E4%BE%8B%E4%B8%8A%E6%89%8B%20Spring%20Boot%20WebFlux%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
