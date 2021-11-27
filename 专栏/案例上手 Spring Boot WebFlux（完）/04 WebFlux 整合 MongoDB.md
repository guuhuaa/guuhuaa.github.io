<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04 WebFlux 整合 MongoDB.md</title>
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

                    <a class="current-tab" href="04&#32;WebFlux&#32;整合&#32;MongoDB.md">04 WebFlux 整合 MongoDB.md</a>
                    

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
                        <div><h1>04 WebFlux 整合 MongoDB</h1>
<h3>前言</h3>
<p>上一课的内容讲解了用 Map 数据结构内存式存储了数据，这样数据就不会持久化，本文我们用 MongoDB 来实现 WebFlux 对数据源的操作。</p>
<p>什么是 MongoDB？<a href="https://www.mongodb.com/">详见官网</a>。</p>
<p>MongoDB 是一个基于分布式文件存储的数据库，由 C++ 语言编写，旨在为 Web 应用提供可扩展的高性能数据存储解决方案。</p>
<p>MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库。</p>
<p>由于操作方便，本文用 Docker 启动一个 MognoDB 服务。如果 Docker 不会安装，请参考此文：<a href="https://www.jianshu.com/p/f272726db9c5">Docker 安装与基本操作</a>。</p>
<p><strong>Docker 安装 MognoDB 并启动如下。</strong></p>
<p>（1）创建挂载目录：</p>
<pre><code>docker volume create mongo_data_db
docker volume create mongo_data_configdb

</code></pre>
<p>（2）启动 MognoDB：</p>
<pre><code>docker run -d \
    --name mongo \
    -v mongo_data_configdb:/data/configdb \
    -v mongo_data_db:/data/db \
    -p 27017:27017 \
    mongo \
    --auth

</code></pre>
<p>（3）初始化管理员账号：</p>
<pre><code>docker exec -it mongo     mongo              admin
                        // 容器名   // mongo命令 数据库名

# 创建最高权限用户
db.createUser({ user: 'admin', pwd: 'admin', roles: [ { role: &quot;root&quot;, db: &quot;admin&quot; } ] });

</code></pre>
<p>（4）测试连通性：</p>
<pre><code>docker run -it --rm --link mongo:mongo mongo mongo -u admin -p admin --authenticationDatabase admin mongo/admin

</code></pre>
<h4>MognoDB 基本操作</h4>
<p>类似 MySQL 命令，显示库列表：</p>
<pre><code>show dbs

</code></pre>
<p>使用某数据库：</p>
<pre><code>use admin

</code></pre>
<p>显示表列表：</p>
<pre><code>show collections

</code></pre>
<p>如果存在 city 表，格式化显示 city 表内容：</p>
<pre><code>db.city.find().pretty()

</code></pre>
<h3>结构</h3>
<p>类似上面讲的工程搭建，新建一个工程编写此案例。工程如图：</p>
<p><img src="assets/02b199c85e5548663557753d48f4b95c1523803.png" alt="img" /></p>
<p>目录核心如下：</p>
<ul>
<li>pom.xml maven 配置；</li>
<li>application.properties 配置文件；</li>
<li>dao 数据访问层，本文要点。</li>
</ul>
<h3>新增 POM 依赖与配置</h3>
<p>在 pom.xml 配置新的依赖：</p>
<pre><code>    &lt;!-- Spring Boot 响应式 MongoDB 依赖 --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
      &lt;artifactId&gt;spring-boot-starter-data-mongodb-reactive&lt;/artifactId&gt;
    &lt;/dependency&gt;

</code></pre>
<p>类似配了 MySQL 和 JDBC 驱动，肯定得去配置数据库。在 application.properties 配置下上面启动的 MongoDB 配置：</p>
<p>数据库名为 admin，账号密码也为 admin。</p>
<pre><code>spring.data.mongodb.host=localhost
spring.data.mongodb.database=admin
spring.data.mongodb.port=27017
spring.data.mongodb.username=admin
spring.data.mongodb.password=admin

</code></pre>
<p>这就一个巨大的问题了，为啥不用我们常用的 MySQL 数据库呢？</p>
<p>答案是 Spring Data Reactive Repositories 目前支持 Mongo、Cassandra、Redis、Couchbase。不支持 MySQL，那究竟为啥呢？那就说明下 JDBC 和 Spring Data 的关系。</p>
<p>Spring Data Reactive Repositories 突出点是 Reactive，即非阻塞的。区别如下：</p>
<ul>
<li>基于 JDBC 实现的 Spring Data，比如 Spring Data JPA 是阻塞的。原理是基于阻塞 IO 模型 消耗每个调用数据库的线程（Connection）。</li>
<li>事务只能在一个 java.sql.Connection 使用，即一个事务一个操作。</li>
</ul>
<p>那如何异步非阻塞封装下 JDBC 的思想也不新鲜，Scala 库 Slick 3 就实现了。简单的实现原理如下：</p>
<ul>
<li>一个事务多个操作，那么共享一个 java.sql.Connection，可以使用透明事务管理，利用回调编程模型去传递。</li>
<li>保持有限的空闲连接。</li>
</ul>
<p>最后，我坚信非阻塞 JDBC 很快就会出现的，这样我们就开心的调用 MySQL 了。</p>
<h3>对象</h3>
<p>修改 org.spring.springboot.domain 包里面的城市实体对象类。修改城市（City）对象 City，代码如下：</p>
<pre><code>import org.springframework.data.annotation.Id;

/**
 * 城市实体类
 *
 */
public class City {

    /**
     * 城市编号
     */
    @Id
    private Long id;

    /**
     * 省份编号
     */
    private Long provinceId;

    /**
     * 城市名称
     */
    private String cityName;

    /**
     * 描述
     */
    private String description;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getProvinceId() {
        return provinceId;
    }

    public void setProvinceId(Long provinceId) {
        this.provinceId = provinceId;
    }

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}

</code></pre>
<p>@Id 注解标记对应库表的主键或者唯一标识符。因为这个是我们的 DO，数据访问对象一一映射到数据存储。</p>
<h3>MongoDB 数据访问层 CityRepository</h3>
<p>修改 CityRepository 类，代码如下：</p>
<pre><code>import org.spring.springboot.domain.City;
import org.springframework.data.mongodb.repository.ReactiveMongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CityRepository extends ReactiveMongoRepository&lt;City, Long&gt; {

}

</code></pre>
<p>CityRepository 接口只要继承 ReactiveMongoRepository 类即可，默认会提供很多实现，比如 CRUD 和列表查询参数相关的实现。ReactiveMongoRepository 接口默认实现了如下：</p>
<pre><code>    &lt;S extends T&gt; Mono&lt;S&gt; insert(S var1);

    &lt;S extends T&gt; Flux&lt;S&gt; insert(Iterable&lt;S&gt; var1);

    &lt;S extends T&gt; Flux&lt;S&gt; insert(Publisher&lt;S&gt; var1);

    &lt;S extends T&gt; Flux&lt;S&gt; findAll(Example&lt;S&gt; var1);

    &lt;S extends T&gt; Flux&lt;S&gt; findAll(Example&lt;S&gt; var1, Sort var2);

</code></pre>
<p>如图，ReactiveMongoRepository 的集成类 ReactiveSortingRepository、ReactiveCrudRepository 实现了很多常用的接口：</p>
<p><img src="assets/40689f2921c9e1289a03e12acef6b80e1523882.png" alt="file" /></p>
<p>ReactiveCrudRepository 接口如图所示：</p>
<p><img src="assets/428841a694e29b128fa99d93bc9fcb391523882.png" alt="img" /></p>
<p>另外可以看出，接口的命名是遵循规范的，常用命名规则如下：</p>
<table>
<thead>
<tr>
<th align="left">关键字</th>
<th align="left">方法命名</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">And</td>
<td align="left">findByNameAndPwd</td>
</tr>
<tr>
<td align="left">Or</td>
<td align="left">findByNameOrSex</td>
</tr>
<tr>
<td align="left">Is</td>
<td align="left">findById</td>
</tr>
<tr>
<td align="left">Between</td>
<td align="left">findByIdBetween</td>
</tr>
<tr>
<td align="left">Like</td>
<td align="left">findByNameLike</td>
</tr>
<tr>
<td align="left">NotLike</td>
<td align="left">findByNameNotLike</td>
</tr>
<tr>
<td align="left">OrderBy</td>
<td align="left">findByIdOrderByXDesc</td>
</tr>
<tr>
<td align="left">Not</td>
<td align="left">findByNameNot</td>
</tr>
</tbody>
</table>
<p>常用案例，代码如下：</p>
<pre><code>    Flux&lt;Person&gt; findByLastname(String lastname);

    @Query(&quot;{ 'firstname': ?0, 'lastname': ?1}&quot;)
    Mono&lt;Person&gt; findByFirstnameAndLastname(String firstname, String lastname);

    // Accept parameter inside a reactive type for deferred execution
    Flux&lt;Person&gt; findByLastname(Mono&lt;String&gt; lastname);

    Mono&lt;Person&gt; findByFirstnameAndLastname(Mono&lt;String&gt; firstname, String lastname);

    @Tailable // Use a tailable cursor
    Flux&lt;Person&gt; findWithTailableCursorBy();

</code></pre>
<h4>源码层面</h4>
<p>ReactiveCrudRepository 抽象在 reactive 包，如图：</p>
<p><img src="assets/ab17d9ea07db0b4fc9b5d310655b98f51523883.png" alt="img" /></p>
<p>这里我们可以看出，支持了 Reactive 还支持了 RxJava。对应老的 CrudRepository 新增了 ReactiveCrudRepository 接口及各种存储实现。</p>
<h3>处理器类 Handler 和控制器类 Controller</h3>
<p>修改下 Handler，代码如下：</p>
<pre><code>@Component
public class CityHandler {

    private final CityRepository cityRepository;

    @Autowired
    public CityHandler(CityRepository cityRepository) {
        this.cityRepository = cityRepository;
    }

    public Mono&lt;City&gt; save(City city) {
        return cityRepository.save(city);
    }

    public Mono&lt;City&gt; findCityById(Long id) {

        return cityRepository.findById(id);
    }

    public Flux&lt;City&gt; findAllCity() {

        return cityRepository.findAll();
    }

    public Mono&lt;City&gt; modifyCity(City city) {

        return cityRepository.save(city);
    }

    public Mono&lt;Long&gt; deleteCity(Long id) {
        cityRepository.deleteById(id);
        return Mono.create(cityMonoSink -&gt; cityMonoSink.success(id));
    }
}

</code></pre>
<p>不要对 Mono、Flux 陌生，把它当成对象即可。继续修改控制器类 Controller，代码如下：</p>
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
<h3>运行工程</h3>
<p>一个 CRUD 的 Spring Boot WebFlux 工程就开发完毕了，下面运行工程验证下。使用 IDEA 右侧工具栏，单击 Maven Project Tab 选项，点击使用 Maven 插件的 install 命令。或者使用命令行的形式，在工程根目录下，执行 Maven 清理和安装工程的指令：</p>
<pre><code>cd springboot-webflux-3-mongodb
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
<p>打开 POST MAN 工具，开发必备。进行下面操作。</p>
<p>新增城市信息 POST http://127.0.0.1:8080/city。</p>
<p><img src="assets/f69fa5b09730de686ef4837824da48e71523883.png" alt="img" /></p>
<h4>连接 MongoDB，验证数据</h4>
<p>连接 MongoDB：</p>
<pre><code>docker run -it --rm --link mongo:mongo mongo mongo -u admin -p admin --authenticationDatabase admin mongo/admin

</code></pre>
<p><img src="assets/5d6d5003dcde1e358ab3a0a47ca08f951523884.png" alt="file" /></p>
<p>显示库列表：</p>
<pre><code>show dbs

</code></pre>
<p>使用某数据库：</p>
<pre><code>use admin

</code></pre>
<p>显示表列表：</p>
<pre><code>show collections

</code></pre>
<p>如果存在 city 表，格式化显示 city 表内容：</p>
<pre><code>db.city.find().pretty()

</code></pre>
<p><img src="assets/093c97deaa04b8855291fcb9765edd011523884.png" alt="img" /></p>
<h3>总结</h3>
<p>这里探讨了 Spring WebFlux 的如何整合 MongoDB，整合其他存储 Cassandra、Redis、Couchbase 就大同小异了。下面，我们已经可以整合 Thymeleaf，更好的页面展示给大家，顺便让大家学习下 Thymeleaf 的基本用法。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;WebFlux&#32;Web&#32;CRUD&#32;实践.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;WebFlux&#32;整合&#32;Thymeleaf.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4355d34ecf645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
