<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05 WebFlux 整合 Thymeleaf.md</title>
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

                    <a class="current-tab" href="05&#32;WebFlux&#32;整合&#32;Thymeleaf.md">05 WebFlux 整合 Thymeleaf.md</a>
                    

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

                    
                    <a href="11&#32;WebFlux&#32;实战图书管理系统.md">11 WebFlux 实战图书管理系统.md</a>

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
                        <div><h1>05 WebFlux 整合 Thymeleaf</h1>
<p>上一篇介绍的是用 MongoDB 来实现 WebFlux 对数据源的操作，那么有了数据需要渲染到前台给用户展示，这就是本文关心的 View 层，View 的表现形式有很多，比如 JSON 和 HTML。开发中常用模板语言很常见的有 Thymeleaf、Freemarker等，那什么是模板语言？</p>
<p>常见的模板语言都包含以下几个概念：数据（Data）、模板（Template）、模板引擎（Template Engine）和结果文档（Result Documents）。</p>
<ul>
<li>数据</li>
</ul>
<p>数据是信息的表现形式和载体，可以是符号、文字、数字、语音、图像、视频等。数据和信息是不可分离的，数据是信息的表达，信息是数据的内涵。数据本身没有意义，数据只有对实体行为产生影响时才成为信息。</p>
<ul>
<li>模板</li>
</ul>
<p>模板，是一个蓝图，即一个与类型无关的类。编译器在使用模板时，会根据模板实参对模板进行实例化，得到一个与类型相关的类。</p>
<ul>
<li>模板引擎</li>
</ul>
<p>模板引擎（这里特指用于 Web 开发的模板引擎）是为了使用户界面与业务数据（内容）分离而产生的，它可以生成特定格式的文档，用于网站的模板引擎就会生成一个标准的 HTML 文档。</p>
<ul>
<li>结果文档</li>
</ul>
<p>一种特定格式的文档，比如用于网站的模板引擎就会生成一个标准的 HTML 文档。</p>
<p>模板语言用途广泛，常见的用途如下：</p>
<ul>
<li>页面渲染</li>
<li>文档生成</li>
<li>代码生成</li>
<li>所有 “数据+模板=文本” 的应用场景</li>
</ul>
<p>Spring Boot 推荐使用的模板语言是 Thymeleaf，那什么是 Thymeleaf？</p>
<p>官方的解释如下：</p>
<pre><code>Thymeleaf is a modern server-side Java template engine for both web and standalone environments.

</code></pre>
<p>Thymeleaf 是现代的模板语言引擎，可以独立运行也可以服务于 Web，主要目标是为开发提供天然的模板，并且能在 HTML 里面准确的显示。</p>
<p>Thymeleaf 是新一代 Java 模板引擎，在 Spring 4 后推荐使用。目前是 Spring 5 自然更加推荐。</p>
<h3>结构</h3>
<p>类似上面讲的工程搭建，新建一个工程编写此案例，工程图如图所示：</p>
<p><img src="assets/3b8c0edab9491e422bef6003299895911524185.png" alt="img" /></p>
<p>目录如下：</p>
<ul>
<li>org.spring.springboot.webflux.controller：Controller 层</li>
<li>org.spring.springboot.dao：数据操作层 DAO</li>
<li>org.spring.springboot.domain：实体类</li>
<li>org.spring.springboot.handler：业务逻辑层</li>
<li>Application：应用启动类</li>
<li>application.properties：应用配置文件</li>
<li>pom.xml maven 配置</li>
<li>application.properties 配置文件</li>
</ul>
<p>模板是会用到下面两个目录：</p>
<ul>
<li>static 目录是存放 CSS、JS 等资源文件；</li>
<li>templates 目录是存放视图。</li>
</ul>
<p>本文重点在 Controller 层 和 templates 视图的编写。</p>
<h3>新增 POM 依赖与配置</h3>
<p>在 pom.xml 配置新的依赖：</p>
<pre><code>  &lt;dependencies&gt;

    &lt;!-- Spring Boot Web Flux 依赖 --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-webflux&lt;/artifactId&gt;
    &lt;/dependency&gt;

    &lt;!-- 模板引擎 Thymeleaf 依赖 --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-thymeleaf&lt;/artifactId&gt;
    &lt;/dependency&gt;

    &lt;!-- Spring Boot Test 依赖 --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
      &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;

    &lt;!-- Junit --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;junit&lt;/groupId&gt;
      &lt;artifactId&gt;junit&lt;/artifactId&gt;
      &lt;version&gt;4.12&lt;/version&gt;
    &lt;/dependency&gt;
  &lt;/dependencies&gt;

</code></pre>
<p>这里我们增加了 Thymeleaf 依赖，但不用在 application.properties - 应用配置文件中配置任何配置。默认启动其默认配置，如需修改配置参考 Thymeleaf 依赖配置，如下：</p>
<pre><code>spring.thymeleaf.cache=true # Enable template caching.
spring.thymeleaf.check-template=true # Check that the template exists before rendering it.
spring.thymeleaf.check-template-location=true # Check that the templates location exists.
spring.thymeleaf.enabled=true # Enable Thymeleaf view resolution for Web frameworks.
spring.thymeleaf.encoding=UTF-8 # Template files encoding.
spring.thymeleaf.excluded-view-names= # Comma-separated list of view names that should be excluded from resolution.
spring.thymeleaf.mode=HTML5 # Template mode to be applied to templates. See also StandardTemplateModeHandlers.
spring.thymeleaf.prefix=classpath:/templates/ # Prefix that gets prepended to view names when building a URL.
spring.thymeleaf.reactive.max-chunk-size= # Maximum size of data buffers used for writing to the response, in bytes.
spring.thymeleaf.reactive.media-types= # Media types supported by the view technology.
spring.thymeleaf.servlet.content-type=text/html # Content-Type value written to HTTP responses.
spring.thymeleaf.suffix=.html # Suffix that gets appended to view names when building a URL.
spring.thymeleaf.template-resolver-order= # Order of the template resolver in the chain.
spring.thymeleaf.view-names= # Comma-separated list of view names that can be resolved.

</code></pre>
<p>包括常用的编码、是否开启缓存等等。</p>
<h3>WebFlux 中使用 Thymeleaf</h3>
<p>在 CityWebFluxController 控制层，添加两个方法如下：</p>
<pre><code>    @GetMapping(&quot;/hello&quot;)
    public Mono&lt;String&gt; hello(final Model model) {
        model.addAttribute(&quot;name&quot;, &quot;泥瓦匠&quot;);
        model.addAttribute(&quot;city&quot;, &quot;浙江温岭&quot;);

        String path = &quot;hello&quot;;
        return Mono.create(monoSink -&gt; monoSink.success(path));
    }

    private static final String CITY_LIST_PATH_NAME = &quot;cityList&quot;;

    @GetMapping(&quot;/page/list&quot;)
    public String listPage(final Model model) {
        final Flux&lt;City&gt; cityFluxList = cityHandler.findAllCity();
        model.addAttribute(&quot;cityList&quot;, cityFluxList);
        return CITY_LIST_PATH_NAME;
    }

</code></pre>
<p>解释下语法：</p>
<ul>
<li>返回值 Mono 或者 String 都行，但是 Mono 代表着我这个返回 View 也是回调的。</li>
<li>return 字符串，该字符串对应的目录在 resources/templates 下的模板名字。</li>
<li>Model 对象来进行数据绑定到视图。</li>
<li>一般会集中用常量管理模板视图的路径。</li>
</ul>
<h3>Tymeleaf 视图</h3>
<p>然后编写两个视图 hello 和 cityList，代码分别如下。</p>
<p>hello.html：</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;zh-CN&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;/&gt;
    &lt;title&gt;欢迎页面&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;

&lt;h1 &gt;你好，欢迎来自&lt;p th:text=&quot;${city}&quot;&gt;&lt;/p&gt;的&lt;p th:text=&quot;${name}&quot;&gt;&lt;/p&gt;&lt;/h1&gt;

&lt;/body&gt;
&lt;/html&gt;

</code></pre>
<p>cityList.html：</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;zh-CN&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;/&gt;
    &lt;title&gt;城市列表&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;

&lt;div&gt;

    &lt;table&gt;
        &lt;legend&gt;
            &lt;strong&gt;城市列表&lt;/strong&gt;
        &lt;/legend&gt;
        &lt;thead&gt;
        &lt;tr&gt;
            &lt;th&gt;城市编号&lt;/th&gt;
            &lt;th&gt;省份编号&lt;/th&gt;
            &lt;th&gt;名称&lt;/th&gt;
            &lt;th&gt;描述&lt;/th&gt;
        &lt;/tr&gt;
        &lt;/thead&gt;
        &lt;tbody&gt;
        &lt;tr th:each=&quot;city : ${cityList}&quot;&gt;
            &lt;td th:text=&quot;${city.id}&quot;&gt;&lt;/td&gt;
            &lt;td th:text=&quot;${city.provinceId}&quot;&gt;&lt;/td&gt;
            &lt;td th:text=&quot;${city.cityName}&quot;&gt;&lt;/td&gt;
            &lt;td th:text=&quot;${city.description}&quot;&gt;&lt;/td&gt;
        &lt;/tr&gt;
        &lt;/tbody&gt;
    &lt;/table&gt;

&lt;/div&gt;

&lt;/body&gt;
&lt;/html&gt;

</code></pre>
<p>常用语法糖如下：</p>
<ul>
<li>${...}：变量表达式；</li>
<li>th:text：处理 Tymeleaf 表达式；</li>
<li>th:each：遍历表达式，可遍历的对象有，实现 java.util.Iterable、java.util.Map（遍历时取 java.util.Map.Entry）、array 等。</li>
</ul>
<p>还有很多使用，可以参考<a href="http://www.thymeleaf.org/documentation.html">官方文档</a>。</p>
<h3>运行工程</h3>
<p>下面运行工程验证下，使用 IDEA 右侧工具栏，点击 Maven Project Tab ，点击使用下 Maven 插件的 install 命令；或者使用命令行的形式，在工程根目录下，执行 Maven 清理和安装工程的指令：</p>
<pre><code>cd springboot-webflux-4-thymeleaf
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
<p>打开浏览器，访问 http://localhost:8080/city/hello ，可以看到如图的响应：</p>
<p><img src="assets/9e0580fa073aa29426bda0aab4f41da51524186.png" alt="img" /></p>
<p>继续访问 http://localhost:8080/city/page/list , 发现没有值，那么按照上一讲插入几条数据即可有值，如图：</p>
<p><img src="assets/66e6502b86c02a83bf56daa93eb9bc1a1524186.png" alt="img" /></p>
<h3>总结</h3>
<p>这里探讨了 Spring WebFlux 的如何整合 Thymeleaf，整合其他模板语言 Thymeleaf、Freemarker，就大同小异了。下面，我们可以整合 Thymeleaf 和 MongoBD 来实现一个整体的简单案例。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;WebFlux&#32;整合&#32;MongoDB.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;WebFlux&#32;中&#32;Thymeleaf&#32;和&#32;MongoDB&#32;实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355d7eb19645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
