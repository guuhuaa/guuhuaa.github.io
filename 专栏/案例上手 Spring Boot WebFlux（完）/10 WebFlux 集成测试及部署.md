<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10 WebFlux 集成测试及部署.md</title>
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

                    <a class="current-tab" href="10&#32;WebFlux&#32;集成测试及部署.md">10 WebFlux 集成测试及部署.md</a>
                    

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
                        <div><h1>10 WebFlux 集成测试及部署</h1>
<h3>前言</h3>
<p>在日常工作中，免不了自测 UT，因为覆盖率不达标，是不允许提交测试，那怎么进行 WebFlux 项目的测试呢。@WebFluxTest 是 WebFlux 测试的重要注解。</p>
<h3>结构</h3>
<p>回到这个工程中，使用 springboot-webflux-3-mongodb 工程，工程如图：</p>
<p><img src="assets/015e1df4d8af293c1ee69c79446b00271525498.png" alt="img" /></p>
<p>目录核心如下：</p>
<ul>
<li>pom.xml 添加 Test 相关依赖；</li>
<li>test / CityWebFluxControllerTest WebFlux API 测试类；</li>
</ul>
<p><a href="https://github.com/JeffLi1993/springboot-learning-example">代码 GiHub 详见这里</a>。</p>
<h3>POM 依赖</h3>
<p>pom.xml 添加对应的测试依赖：</p>
<pre><code>    &lt;!-- Spring Boot Test 依赖 --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
      &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;

    &lt;dependency&gt;
      &lt;groupId&gt;io.projectreactor&lt;/groupId&gt;
      &lt;artifactId&gt;reactor-test&lt;/artifactId&gt;
      &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;

</code></pre>
<h3>CityWebFluxControllerTest WebFlux API 测试类</h3>
<p>@WebFluxTest 用于测试 Spring WebFlux 控制器，支持自动配置 Spring WebFlux 基础组件，可以限制扫描范围等。</p>
<p>代码如下：</p>
<pre><code>@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class CityWebFluxControllerTest {

    @Autowired
    private WebTestClient webClient;

    private static Map&lt;String, City&gt; cityMap = new HashMap&lt;&gt;();

    @BeforeClass
    public static void setup() throws Exception {
        City wl = new City();
        wl.setId(1L);
        wl.setProvinceId(2L);
        wl.setCityName(&quot;WL&quot;);
        wl.setDescription(&quot;WL IS GOOD&quot;);
        cityMap.put(&quot;WL&quot;, wl);
    }

    @Test
    public void testSave() throws Exception {

        City expectCity = webClient.post().uri(&quot;/city&quot;)
                .contentType(MediaType.APPLICATION_JSON)
                .body(BodyInserters.fromObject(cityMap.get(&quot;WL&quot;)))
                .exchange()
                .expectStatus().isOk()
                .expectBody(City.class).returnResult().getResponseBody();

        Assert.assertNotNull(expectCity);
        Assert.assertEquals(expectCity.getId(), cityMap.get(&quot;WL&quot;).getId());
        Assert.assertEquals(expectCity.getCityName(), cityMap.get(&quot;WL&quot;).getCityName());
    }

}

</code></pre>
<p>代码详解：</p>
<ul>
<li>@WebFluxTest 注入了 WebTestClient 对象，用于测试 WebFlux 控制器，好处是快速，并无需启动完整 HTTP 容器。</li>
<li>WebTestClient.post() 方法构造了 POST 测试请求，并使用 uri 指定路由。</li>
<li>expectStatus() 用于验证返回状态是否为 ok()，即 200 返回码。</li>
<li>expectBody(City.class) 用于验证返回对象体是为 City 对象，并利用 returnResult 获取对象。</li>
<li>Assert 是以前我们常用的断言方法验证测试结果。</li>
</ul>
<p>运行 Test，得到如图验证结果：</p>
<p><img src="assets/da3ec656da4450f7042ecd20238735401525498.png" alt="file" /></p>
<h3>工程运行方式</h3>
<p>了解工程服务器部署，先了解工程如何运行。</p>
<p>上面使用应用启动类运行工程，这是其中一种工程运行方式。Spring Boot 应用的运行方式很简单，下面介绍下这三种运行方式。</p>
<h4>1. 使用应用启动类</h4>
<p>在 IDEA 中直接执行应用启动类，来运行 Spring Boot 应用，日常开发中，会经常使用这种方式启动应用。常用的会有 Debug 启动模式，方便在开发中进行代码调试和 bug 处理。自然，Debug 启动模式会比正常模式稍微慢一些。</p>
<h4>2. 使用 Maven 运行</h4>
<p>通过 Maven 运行，需要配置 Spring Boot Maven 插件，在 pom.xml 配置文件中，新增 build 节点并配置插件 spring-boot-maven-plugin，代码如下：</p>
<pre><code>&lt;build&gt;
    &lt;plugins&gt;
        &lt;!-- Spring Boot Maven 插件 --&gt;
        &lt;plugin&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
        &lt;/plugin&gt;
    &lt;/plugins&gt;
&lt;/build&gt;

</code></pre>
<p>在工程根目录中，运行如下 Maven 命令来运行 Spring Boot 应用：</p>
<pre><code>mvn spring-boot:run

</code></pre>
<p>实际调用的是 pom.xml 配置的 Spring Boot Maven 插件 spring-boot-maven-plugin，上面执行了插件提供的 run 指令。也可以在 IDEA 右侧工具栏的 Maven Project Tab 中，找到 Maven 插件的 spring-boot-maven-plugin，执行相应的指令。所有指令如下：</p>
<pre><code># 生成构建信息文件
spring-boot:build-info
# 帮助信息
spring-boot:help
# 重新打包
spring-boot:repackage
# 运行工程
spring-boot:run
# 将工程集成到集成测试阶段，进行工程的声明周期管理
spring-boot:start
spring-boot:stop

</code></pre>
<h4>3. 使用 Java 命令运行</h4>
<p>使用 Maven 或者 Gradle 安装工程，生成可执行的工程 jar 后，运行如下 Java 命令来运行 Spring Boot 应用：</p>
<pre><code>java -jar target/xxx.jar 

</code></pre>
<p>这里运行了 spring-boot-maven-plugin 插件编译出来的可执行 jar 文件。通过上述三种方式都可以成功运行 Spring Boot 工程，成功运行输出的控制台信息如图 1-10 所示。</p>
<p><img src="assets/0f234db300ec389786b1a7e55b7bb5ec1515130.png" alt="img" /></p>
<h3>工程服务器部署</h3>
<p>基础环境安装如上面说的，需要 JDK 环境、Maven 环境等。</p>
<h4>Win 服务器</h4>
<p>推荐使用 AlwaysUp：</p>
<p><img src="assets/91b7d3d4b629f5b7475b7b0d92f3db491516073.png" alt="img" /></p>
<p>使用方式也很简单：</p>
<p><img src="assets/24b98badfdad8d24bd5a1c46c3e012fd1516073.png" alt="img" /></p>
<h4>Linux 服务器</h4>
<p>推荐 yum 安装基础环境，比如安装 JDK：</p>
<pre><code>yum -y list java*
yum -y install java-1.8.0-openjdk*
java -version 

</code></pre>
<p>安装 Maven：</p>
<pre><code>yum -y list apache-maven
sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
sudo yum install -y apache-maven
mvn --v

</code></pre>
<p>Linux 使用 nohup 命令进行对后台程序的启动关闭。</p>
<p>关闭应用的脚本：stop.sh</p>
<p><img src="assets/87aed0bf416fc6ed134bf324f744558b1516073.png" alt="img" /></p>
<p>启动应用的脚本：start.sh</p>
<p><img src="assets/c1b800203d816380d24b03c9b4f72a311516073.png" alt="img" /></p>
<p>重启应用的脚本：stop.sh</p>
<p><img src="assets/712242d8401da8fa9b9842628890ed2a1516073.png" alt="img" /></p>
<h3>总结</h3>
<p>这一篇主要一起实践了简单的 WebFlux API 控制层的测试，Service 测试 Mock 和以前一样，以及工程运行、服务器部署的操作。</p>
<p>工程：springboot-webflux-9-test。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;WebFlux&#32;中&#32;WebSocket&#32;实现通信.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;WebFlux&#32;实战图书管理系统.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355f0bca9645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
