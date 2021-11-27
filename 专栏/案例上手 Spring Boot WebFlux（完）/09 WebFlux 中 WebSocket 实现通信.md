<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>09 WebFlux 中 WebSocket 实现通信.md</title>
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

                    <a class="current-tab" href="09&#32;WebFlux&#32;中&#32;WebSocket&#32;实现通信.md">09 WebFlux 中 WebSocket 实现通信.md</a>
                    

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
                        <div><h1>09 WebFlux 中 WebSocket 实现通信</h1>
<h3>前言</h3>
<p>WebFlux 该模块中包含了对反应式 HTTP、服务器推送事件和 WebSocket 的客户端和服务器端的支持。这里我们简单实践下 WebFlux 中 WebSocket 实现通信。</p>
<h3>什么是 WebSocket</h3>
<p>WebSocket 是一种通信协议，类比下 HTTP 协议，HTTP 协议只能有客户端发起请求，然后得到响应。 一般通过 HTTP 的轮询方式，实现 WebSocket 类似功能。</p>
<p>因为轮询，每次新建连接，请求响应，浪费资源。WebSocket 就出现了，它支持客户端和服务端双向通讯。类似 http 和 https，WebSocket 的标识符为 ws 和 wss，案例地址为：</p>
<pre><code>ws://localhost:8080/echo

</code></pre>
<h3>结构</h3>
<p>回到这个工程，新建一个工程编写 WebSocket 实现通信案例。工程如图：</p>
<p><img src="assets/38520c5f22d961494869d108b3c044711525329.png" alt="file" /></p>
<p>目录核心如下：</p>
<ul>
<li>EchoHandler websocket 处理类（类似 HTTP Servlet 处理）</li>
<li>WebSocketConfiguration websocket 配置类</li>
<li>websocket-client.html HTML 客户端实现</li>
<li>WSClient java 客户端实现</li>
</ul>
<p><a href="https://github.com/JeffLi1993/springboot-learning-example">单击这里查看源代码</a>。</p>
<h3>EchoHandler 处理类</h3>
<p>代码如下：</p>
<pre><code>import org.springframework.stereotype.Component;
import org.springframework.web.reactive.socket.WebSocketHandler;
import org.springframework.web.reactive.socket.WebSocketSession;
import reactor.core.publisher.Mono;

@Component
public class EchoHandler implements WebSocketHandler {
    @Override
    public Mono&lt;Void&gt; handle(final WebSocketSession session) {
        return session.send(
                session.receive()
                        .map(msg -&gt; session.textMessage(
                                &quot;服务端返回：小明， -&gt; &quot; + msg.getPayloadAsText())));
    }
}

</code></pre>
<p>代码详解：</p>
<ul>
<li>WebSocketHandler 接口，实现该接口来处理 WebSokcet 消息。</li>
<li>handle(WebSocketSession session) 方法，接收 WebSocketSession 对象，即获取客户端信息、发送消息和接收消息的操作对象。</li>
<li>receive() 方法，接收消息，使用 map 操作获取的 Flux 中包含的消息持续处理，并拼接出返回消息 Flux 对象。</li>
<li>send() 方法，发送消息。消息为“服务端返回：小明， -&gt; ”开头的。</li>
</ul>
<h3>WebSocketConfiguration 配置类</h3>
<p>代码如下：</p>
<pre><code>@Configuration
public class WebSocketConfiguration {

    @Autowired
    @Bean
    public HandlerMapping webSocketMapping(final EchoHandler echoHandler) {
        final Map&lt;String, WebSocketHandler&gt; map = new HashMap&lt;&gt;();
        map.put(&quot;/echo&quot;, echoHandler);

        final SimpleUrlHandlerMapping mapping = new SimpleUrlHandlerMapping();
        mapping.setOrder(Ordered.HIGHEST_PRECEDENCE);
        mapping.setUrlMap(map);
        return mapping;
    }

    @Bean
    public WebSocketHandlerAdapter handlerAdapter() {
        return new WebSocketHandlerAdapter();
    }
}

</code></pre>
<p>代码详解：</p>
<ul>
<li>WebSocketHandlerAdapter 负责将 EchoHandler 处理类适配到 WebFlux 容器中；</li>
<li>SimpleUrlHandlerMapping 指定了 WebSocket 的路由配置；</li>
<li>使用 map 指定 WebSocket 协议的路由，路由为 ws://localhost:8080/echo。</li>
</ul>
<h3>运行工程</h3>
<p>一个操作 Redis 工程就开发完毕了，下面运行工程验证下。使用 IDEA 右侧工具栏，点击 Maven Project Tab，点击使用下 Maven 插件的 install 命令。或者使用命令行的形式，在工程根目录下，执行 Maven 清理和安装工程的指令：</p>
<pre><code>cd springboot-webflux-8-websocket
mvn clean install

</code></pre>
<p>在控制台中看到成功的输出：</p>
<pre><code>... 省略
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 01:30 min
[INFO] Finished at: 2018-10-15T10:00:54+08:00
[INFO] Final Memory: 31M/174M
[INFO] ------------------------------------------------------------------------

</code></pre>
<p>在 IDEA 中执行 Application 类启动，任意正常模式或者 Debug 模式，可以在控制台看到成功运行的输出：</p>
<pre><code>... 省略
2018-04-10 08:43:39.932  INFO 2052 --- [ctor-http-nio-1] r.ipc.netty.tcp.BlockingNettyContext     : Started HttpServer on /0:0:0:0:0:0:0:0:8080
2018-04-10 08:43:39.935  INFO 2052 --- [           main] o.s.b.web.embedded.netty.NettyWebServer  : Netty started on port(s): 8080
2018-04-10 08:43:39.960  INFO 2052 --- [           main] org.spring.springboot.Application        : Started Application in 6.547 seconds (JVM running for 9.851)

</code></pre>
<p>打开 <a href="https://www.websocket.org/echo.html">https://www.websocket.org/echo.html</a>网页，大多数浏览器是支持 WebSokcet 协议的。</p>
<p>Location - 输入通信地址、点击 Conect 会出现 CONNECTED。</p>
<p>然后发送消息，可以看到服务端返回对应的消息。如果此时关闭了服务端，那么会出现 DISCONNECTED：</p>
<p><img src="assets/39b8cd4ff4872ca11fd091744c83e5171525330.png" alt="file" /></p>
<h3>websocket-client.html HTML 客户端实现</h3>
<p>实现 HTML 客户端：</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;title&gt;Client WebSocket&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;div class=&quot;chat&quot;&gt;&lt;/div&gt;

&lt;script&gt;
  var clientWebSocket = new WebSocket(&quot;ws://localhost:8080/echo&quot;);

  clientWebSocket.onopen = function () {
    console.log(&quot;clientWebSocket.onopen&quot;, clientWebSocket);
    console.log(&quot;clientWebSocket.readyState&quot;, &quot;websocketstatus&quot;);
    clientWebSocket.send(&quot;你好！&quot;);
  }

  clientWebSocket.onclose = function (error) {
    console.log(&quot;clientWebSocket.onclose&quot;, clientWebSocket, error);
    events(&quot;聊天会话关闭！&quot;);
  }

  function events(responseEvent) {
    document.querySelector(&quot;.chat&quot;).innerHTML += responseEvent + &quot;&lt;br&gt;&quot;;
  }
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

</code></pre>
<p>大多数浏览器是支持 WebSocket，代码详解如下：</p>
<ul>
<li>网页打开是，会调用 onopen 方法，并发送消息给服务端“你好！”；</li>
<li>如果服务端关闭，会调用 onclose 方法，页面会出现“聊天会话关闭！”信息。</li>
</ul>
<h3>WSClient Java 客户端实现</h3>
<p>类似，HTTPClient 调用 HTTP，WebSocket 客户端去调用 WebSokcet 协议，并实现服务。代码如下：</p>
<pre><code>public class WSClient {
    public static void main(final String[] args) {
        final WebSocketClient client = new ReactorNettyWebSocketClient();
        client.execute(URI.create(&quot;ws://localhost:8080/echo&quot;), session -&gt;
                session.send(Flux.just(session.textMessage(&quot;你好&quot;)))
                        .thenMany(session.receive().take(1).map(WebSocketMessage::getPayloadAsText))
                        .doOnNext(System.out::println)
                        .then())
                .block(Duration.ofMillis(5000));
    }
}

</code></pre>
<p>代码详解：</p>
<ul>
<li>ReactorNettyWebSocketClient 是 WebFlux 默认 Reactor Netty 库提供的 WebSocketClient 实现。</li>
<li>execute 方法，与 ws://localhost:8080/echo 建立 WebSokcet 协议连接。</li>
<li>execute 需要传入 WebSocketHandler 的对象，用来处理消息，这里的实现和前面的 EchoHandler 类似。</li>
<li>通过 WebSocketSession 的 send 方法来发送字符串“你好”到服务器端，然后通过 receive 方法来等待服务器端的响应并输出。</li>
</ul>
<h3>总结</h3>
<p>这一篇内容主要一起实践了简单的 WebSocket 的应用操作，以及 WebSocket 客户端小例子。</p>
<p>工程：springboot-webflux-8-websocket</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="08&#32;WebFlux&#32;中&#32;Redis&#32;实现缓存.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="10&#32;WebFlux&#32;集成测试及部署.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355ec2856645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
