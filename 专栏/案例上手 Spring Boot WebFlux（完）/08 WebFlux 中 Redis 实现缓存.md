<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>08 WebFlux 中 Redis 实现缓存.md</title>
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

                    <a class="current-tab" href="08&#32;WebFlux&#32;中&#32;Redis&#32;实现缓存.md">08 WebFlux 中 Redis 实现缓存.md</a>
                    

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
                        <div><h1>08 WebFlux 中 Redis 实现缓存</h1>
<h3>前言</h3>
<p>首先，补充下上一篇的内容，RedisTemplate 实现操作 Redis，但操作是同步的，不是 Reactive 的。自然，支持 Reactive 的操作类为 ReactiveRedisTemplate，下面我们写个小案例。</p>
<h3>ReactiveRedisTemplate</h3>
<p>在上一篇工程中，新建 CityWebFluxReactiveController 类，路由为 /city2 开头。</p>
<pre><code>@RestController
@RequestMapping(value = &quot;/city2&quot;)
public class CityWebFluxReactiveController {

    @Autowired
    private ReactiveRedisTemplate reactiveRedisTemplate;

    @GetMapping(value = &quot;/{id}&quot;)
    public Mono&lt;City&gt; findCityById(@PathVariable(&quot;id&quot;) Long id) {
        String key = &quot;city_&quot; + id;
        ReactiveValueOperations&lt;String, City&gt; operations = reactiveRedisTemplate.opsForValue();
        Mono&lt;City&gt; city = operations.get(key);
        return city;
    }

    @PostMapping
    public Mono&lt;City&gt; saveCity(@RequestBody City city) {
        String key = &quot;city_&quot; + city.getId();
        ReactiveValueOperations&lt;String, City&gt; operations = reactiveRedisTemplate.opsForValue();
        return operations.getAndSet(key, city);
    }

    @DeleteMapping(value = &quot;/{id}&quot;)
    public Mono&lt;Long&gt; deleteCity(@PathVariable(&quot;id&quot;) Long id) {
        String key = &quot;city_&quot; + id;
        return reactiveRedisTemplate.delete(key);
    }
}

</code></pre>
<ul>
<li>写法和以前保持一致，@Autowired 注入 ReactiveRedisTemplate 对象。</li>
<li>ReactiveValueOperations 是 String（或 value）的操作视图，操作视图还有 ReactiveHashOperations、ReactiveListOperations、ReactiveSetOperations 和 ReactiveZSetOperations 等。</li>
<li>不一样的是，操作视图 set 方法是操作 City 对象，但可以 get 回 Mono 或者 Flux 对象。</li>
</ul>
<h3>结构</h3>
<p>回到这个工程，新建一个工程编写整合 Redis 实现缓存案例，工程如图：</p>
<p><img src="assets/3b4f95fda4771ca70c5bbc644f82a0c01525318.png" alt="file" /></p>
<p>目录核心如下：</p>
<ul>
<li>pom.xml maven 配置</li>
<li>application.properties 配置文件</li>
<li>domain 实体类</li>
<li>dao mongodb数据操作层</li>
<li>handler 业务层，本文要点</li>
<li>controller 控制层</li>
</ul>
<p><a href="https://github.com/JeffLi1993/springboot-learning-example">单击这里查看源代码</a>。</p>
<h3>控制层 CityWebFluxController</h3>
<p>代码如下：</p>
<pre><code>@RestController
@RequestMapping(value = &quot;/city&quot;)
public class CityWebFluxController {

    @Autowired
    private CityHandler cityHandler;

    @GetMapping(value = &quot;/{id}&quot;)
    public Mono&lt;City&gt; findCityById(@PathVariable(&quot;id&quot;) Long id) {
        return cityHandler.findCityById(id);
    }

    @GetMapping()
    public Flux&lt;City&gt; findAllCity() {
        return cityHandler.findAllCity();
    }

    @PostMapping()
    public Mono&lt;City&gt; saveCity(@RequestBody City city) {
        return cityHandler.save(city);
    }

    @PutMapping()
    public Mono&lt;City&gt; modifyCity(@RequestBody City city) {
        return cityHandler.modifyCity(city);
    }

    @DeleteMapping(value = &quot;/{id}&quot;)
    public Mono&lt;Long&gt; deleteCity(@PathVariable(&quot;id&quot;) Long id) {
        return cityHandler.deleteCity(id);
    }
}

</code></pre>
<h3>CityHandler 业务层</h3>
<p>目前，@Cacheable 等注解形式实现缓存没有很好的集成，二者 Mono / Flux 对象没有实现 Serializable，无法通过默认序列化器，解决方式是需要自定义序列化，这里通过手动方式与 Redis 手动集成，并实现缓存策略。</p>
<p><a href="http://coolshell.cn/articles/17416.html">参考《缓存更新的套路》</a>，缓存更新的模式有四种：Cache aside、Read through、Write through、Write behind caching。</p>
<p>这里使用的是 Cache Aside 策略，从三个维度（摘自耗子叔叔博客）：</p>
<ul>
<li>失效：应用程序先从 Cache 取数据，没有得到，则从数据库中取数据，成功后，放到缓存中。</li>
<li>命中：应用程序从 Cache 中取数据，取到后返回。</li>
<li>更新：先把数据存到数据库中，成功后，再让缓存失效。</li>
</ul>
<p>代码如下：</p>
<pre><code>@Component
public class CityHandler {

    private static final Logger LOGGER = LoggerFactory.getLogger(CityHandler.class);

    @Autowired
    private RedisTemplate redisTemplate;

    private final CityRepository cityRepository;

    @Autowired
    public CityHandler(CityRepository cityRepository) {
        this.cityRepository = cityRepository;
    }

    public Mono&lt;City&gt; save(City city) {
        return cityRepository.save(city);
    }

    public Mono&lt;City&gt; findCityById(Long id) {

        // 从缓存中获取城市信息
        String key = &quot;city_&quot; + id;
        ValueOperations&lt;String, City&gt; operations = redisTemplate.opsForValue();

        // 缓存存在
        boolean hasKey = redisTemplate.hasKey(key);
        if (hasKey) {
            City city = operations.get(key);

            LOGGER.info(&quot;CityHandler.findCityById() : 从缓存中获取了城市 &gt;&gt; &quot; + city.toString());
            return Mono.create(cityMonoSink -&gt; cityMonoSink.success(city));
        }

        // 从 MongoDB 中获取城市信息
        Mono&lt;City&gt; cityMono = cityRepository.findById(id);

        if (cityMono == null)
            return cityMono;

        // 插入缓存
        cityMono.subscribe(cityObj -&gt; {
            operations.set(key, cityObj);
            LOGGER.info(&quot;CityHandler.findCityById() : 城市插入缓存 &gt;&gt; &quot; + cityObj.toString());
        });

        return cityMono;
    }

    public Flux&lt;City&gt; findAllCity() {
        return cityRepository.findAll().cache();
    }

    public Mono&lt;City&gt; modifyCity(City city) {

        Mono&lt;City&gt; cityMono = cityRepository.save(city);

        // 缓存存在，删除缓存
        String key = &quot;city_&quot; + city.getId();
        boolean hasKey = redisTemplate.hasKey(key);
        if (hasKey) {
            redisTemplate.delete(key);

            LOGGER.info(&quot;CityHandler.modifyCity() : 从缓存中删除城市 ID &gt;&gt; &quot; + city.getId());
        }

        return cityMono;
    }

    public Mono&lt;Long&gt; deleteCity(Long id) {

        cityRepository.deleteById(id);

        // 缓存存在，删除缓存
        String key = &quot;city_&quot; + id;
        boolean hasKey = redisTemplate.hasKey(key);
        if (hasKey) {
            redisTemplate.delete(key);

            LOGGER.info(&quot;CityHandler.deleteCity() : 从缓存中删除城市 ID &gt;&gt; &quot; + id);
        }

        return Mono.create(cityMonoSink -&gt; cityMonoSink.success(id));
    }
}

</code></pre>
<p>首先这里注入了 RedisTemplate 对象，联想到 Spring 的 JdbcTemplate ，RedisTemplate 封装了 RedisConnection，具有连接管理，序列化和 Redis 操作等功能，还有针对 String 的支持对象 StringRedisTemplate。</p>
<p>回到更新缓存的逻辑。</p>
<p>a. findCityById 获取城市逻辑：</p>
<ul>
<li>如果缓存存在，从缓存中获取城市信息；</li>
<li>如果缓存不存在，从 DB 中获取城市信息，然后插入缓存。</li>
</ul>
<p>b. deleteCity 删除 / modifyCity 更新城市逻辑：</p>
<ul>
<li>如果缓存存在，删除；</li>
<li>如果缓存不存在，不操作。</li>
</ul>
<h3>运行工程</h3>
<p>一个操作 Redis 工程就开发完毕了，下面运行工程验证下。使用 IDEA 右侧工具栏，点击 Maven Project Tab，点击使用下 Maven 插件的 install 命令；或者使用命令行的形式，在工程根目录下，执行 Maven 清理和安装工程的指令：</p>
<pre><code>cd springboot-webflux-7-redis-cache
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
<p>打开 POST MAN 工具，开发必备。进行下面操作：</p>
<p><strong>新增城市信息 POST http://127.0.0.1:8080/city</strong></p>
<p><img src="assets/f69fa5b09730de686ef4837824da48e71523883-1608971278890.png" alt="file" /></p>
<p><strong>获取城市信息 GET http://127.0.0.1:8080/city/2</strong></p>
<p><img src="assets/2e129648b8e574a54ff7940f00f1dc591524819-1608971278898.png" alt="file" /></p>
<p>再请求一次，获取城市信息会发现数据获取的耗时快了很多，服务端 Console 输出的日志：</p>
<pre><code>2017-04-13 18:29:00.273  INFO 13038 --- [nio-8080-exec-1] findCityById() : 城市插入缓存 &gt;&gt; City{id=12, provinceId=3, cityName='三亚', description='水好,天蓝'}
2017-04-13 18:29:03.145  INFO 13038 --- [nio-8080-exec-2] findCityById() : 从缓存中获取了城市 &gt;&gt; City{id=12, provinceId=3, cityName='三亚', description='水好,天蓝'}

</code></pre>
<p>可见，第一次是从数据库 MongoDB 获取数据，并插入缓存，第二次直接从缓存中取。</p>
<p>更新 / 删除城市信息，这两种操作中，如果缓存有对应的数据，则删除缓存。服务端 Console 输出的日志：</p>
<pre><code>2017-04-13 18:29:52.248  INFO 13038 --- [nio-8080-exec-9] deleteCity() : 从缓存中删除城市 ID &gt;&gt; 12

</code></pre>
<h3>总结</h3>
<p>这一讲，主要补充了 Redis 对响应式的支持操作，以及缓存更新策略及实际应用小例子。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="07&#32;WebFlux&#32;整合&#32;Redis.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="09&#32;WebFlux&#32;中&#32;WebSocket&#32;实现通信.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355e7dcf5645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
