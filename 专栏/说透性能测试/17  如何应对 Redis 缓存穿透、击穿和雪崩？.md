<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17  如何应对 Redis 缓存穿透、击穿和雪崩？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么每个测试人都要学好性能测试？.md">00 开篇词  为什么每个测试人都要学好性能测试？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;JMeter&#32;的核心概念.md">01  JMeter 的核心概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;JMeter&#32;参数化策略.md">02  JMeter 参数化策略.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;构建并执行&#32;JMeter&#32;脚本的正确姿势.md">03  构建并执行 JMeter 脚本的正确姿势.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;JMeter&#32;二次开发其实并不难.md">04  JMeter 二次开发其实并不难.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">05  如何基于 JMeter API 开发性能测试平台？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Nginx&#32;在系统架构中的作用.md">06  Nginx 在系统架构中的作用.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;你真的知道如何制定性能测试的目标吗？.md">07  你真的知道如何制定性能测试的目标吗？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;性能测试场景的分类和意义.md">08  性能测试场景的分类和意义.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;如何制定一份有效的性能测试方案？.md">09  如何制定一份有效的性能测试方案？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;命令行监控&#32;Linux&#32;服务器的要点.md">10  命令行监控 Linux 服务器的要点.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;分布式服务链路监控以及报警方案.md">11  分布式服务链路监控以及报警方案.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何把可视化监控也做得酷炫？.md">12  如何把可视化监控也做得酷炫？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;Docker&#32;的制作、运行以及监控.md">13  Docker 的制作、运行以及监控.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何从&#32;CPU&#32;飙升定位到热点方法？.md">14  如何从 CPU 飙升定位到热点方法？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何基于&#32;JVM&#32;分析内存使用对象？.md">15  如何基于 JVM 分析内存使用对象？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;如何通过&#32;Arthas&#32;定位代码链路问题？.md">16  如何通过 Arthas 定位代码链路问题？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="17&#32;&#32;如何应对&#32;Redis&#32;缓存穿透、击穿和雪崩？.md">17  如何应对 Redis 缓存穿透、击穿和雪崩？.md</a>
                    

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何才能优化&#32;MySQL&#32;性能？.md">18  如何才能优化 MySQL 性能？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何根治慢&#32;SQL？.md">19  如何根治慢 SQL？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;线上全链路性能测试实践总结.md">20 结束语  线上全链路性能测试实践总结.md</a>

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
                        <div><h1>17  如何应对 Redis 缓存穿透、击穿和雪崩？</h1>
<p>上一讲我带你学习了如何应用 Arthas 定位代码以及链路问题。这一讲我将带你来学习一个关键的内存数据库中间件 Redis，希望你可以了解它的作用，以及在使用过程中的常见问题以及解决方案。</p>
<h3>为什么使用内存数据库？</h3>
<p>首先我们来看看最早期的 Web 架构是什么样的，如图 1 所示：</p>
<p><img src="assets/Cgp9HWA_jkyAW6_xAABZGKmSgp0617.png" alt="1.png" /></p>
<p>图 1：早期架构</p>
<p>这是互联网早期的常用架构，不过这样的架构一般只满足于基本的业务运转，一旦业务量迅速增高，就会出现各种<strong>请求延迟</strong>，甚至<strong>超时响应</strong>或者<strong>直接请求拒绝</strong>的情况 ，也就是在高访问量下会发生性能问题，而且这样的框架性能问题又集中在<strong>数据库层面</strong>。</p>
<p>那么问题来了，为什么会产生这种情况呢？由于数据库的数据是存在硬盘上，硬盘的 I/O 读写瓶颈会直接影响<strong>并发量</strong>。既然磁盘 I/O 读写时瓶颈，我们是不是可以采用速度更快的内存来<strong>存储常用但数据量不算大的数据</strong>呢？答案是肯定的。</p>
<p>为了解决上面的问题，目前通用的做法是<strong>引入基于内存的数据库</strong>，这样的数据库一般是把数据先放到内存里，引入缓存中间件之后的项目 Web 服务架构图如下所示：</p>
<p><img src="assets/Cgp9HWA_jl-AZ0_0AAC_NrxVK8s022.png" alt="2.png" /></p>
<p>图 2：演变架构</p>
<p>这样便可以较大程度缓解传统数据库带来的磁盘 I/O 读写瓶颈，而我们最常使用的基于内存的数据库就是 <strong>Redis</strong> 和 <strong>MemCached</strong>。</p>
<h3>Redis 和 Memcached 对比</h3>
<h4>1.存储方式</h4>
<ul>
<li>MemCached 目前只支持<strong>单一的数据结构 Key-Value 形式</strong>；</li>
<li>Redis 支持<strong>多种数据结构</strong>，有字符串、列表、集合、散列表、有序集合等。</li>
</ul>
<h4><strong>2.持久化</strong></h4>
<p><strong>持久化就是把数据从内存永久存储到磁盘里</strong>，可以防止断电等异常情况下数据丢失等问题。目前 Redis 支持持久化，而 MemCached 不支持。遇到灾难，MemCached 无法恢复数据，<strong>Redis 可以恢复数据</strong>，<strong>保证了数据的安全性</strong>。</p>
<p>从以上特点可以看出 Redis 在<strong>数据多样性</strong>和<strong>安全性</strong>上远高于 MemCached。以我的从业经历讲，MemCachded 使用频率越来越低，绝大多数的业务场景使用 Redis 居多。</p>
<h3>Redis 带来的性能影响</h3>
<p>我们列举一个案例来看 Redis 带来的性能影响。</p>
<p>我们使用 Spring Boot 开发连接 Redis 的 demo，分如下三步。</p>
<p>（1）在 Maven 中引入 Spring Boot 使用的 Redis 类库，如下代码所示：</p>
<pre><code>&lt;dependency&gt;

   &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

   &lt;artifactId&gt;spring-boot-starter-data-redis&lt;/artifactId&gt;

   &lt;version&gt;2.4.2&lt;/version&gt;

&lt;/dependency&gt;
</code></pre>
<p>（2）通过注解方式获取 RedisTemplate，如下代码所示：</p>
<pre><code>@Autowired

private RedisTemplate&lt;String, String&gt; redisTemplate;
</code></pre>
<p>（3）使用 Redis 提供的 API 实现业务代码的缓存读写，如下代码所示：</p>
<pre><code>@GetMapping(&quot;/getRedisTestData&quot;)

public Result getRedisTestData(){

    String redisTestListData = null;

    try {

        redisTestListData = redisTemplate.boundValueOps(&quot;redisTest.findAll&quot;).get();

        //如果redis中没有数据的话

        if(null == redisTestListData){

            //查询数据库获得数据

            List&lt;RedisTest&gt; redisTestList = simulateSceneRepository.findAll();

            //转换成json格式字符串

            ObjectMapper om = new ObjectMapper();

            redisTestListData = om.writeValueAsString(redisTestList);

            //将数据存储到redis中，下次在查询直接从redis中获得数据，不用再查询数据库

            redisTemplate.boundValueOps(&quot;redisTest.findAll&quot;).set(redisTestListData);

            log.info(&quot;从Mysql数据库获得数据&quot;);

        }else{

            log.info(&quot;从redis缓存中获得数据&quot;);

        }

    } catch (Exception e){

        log.error(&quot;e:{}&quot;,e);

    }

    return Result.resultSuccess(null,redisTestListData,&quot;数据读取成功&quot;);

}
</code></pre>
<p>通过如上三步就可以完成 Java 使用 Redis 的 demo，我大概总结下代码流程，第一次先判断 Redis 中是否存在查询的数据，如果没有就需要从数据库中读取数据了，读取成功之后把数据回写到 Redis 中，后面的请求就能直接从 Redis 中直接读取了，较大地减少了对数据库的查询压力。我们可以通过运行上面写好的代码来看下实际效果。</p>
<p>首先我们向数据表 redis_test 插入 10w 条数据，然后分两次访问该接口，对比下两次访问的响应时间。</p>
<p>第一次直接从 MySQL 数据库读取，一共花了 39.43s，如下图所示：</p>
<p><img src="assets/Cgp9HWA9DVKAYW32AAFDyYw_tDs126.png" alt="Drawing 2.png" /></p>
<p>图 3：MySQL 取数据耗时</p>
<p>而第二次数据已经进入 Redis，请求只需要 2.62s，节省了很长时间。值得注意的是为了演示效果，取出的数据条数达到 10w+，所以响应时间也达到了秒级别。在正常的互联网业务当中，Redis 读写操作均在毫秒级别。</p>
<p><img src="assets/CioPOWA9DVmACUdmAAFWomKWRnk641.png" alt="Drawing 3.png" /></p>
<p>图 4：Redis 取数据耗时</p>
<p>从上面实例可以看出使用 Redis 和不使用 Redis <strong>性能差距明显</strong>，所以从目前的互联网项目来讲，使用 Redis 是一个非常普遍的情况，接下来我们来了解下 Redis 其他特性和优缺点。</p>
<h3>Redis 其他特性以及优缺点</h3>
<h4>1.Redis 的特性</h4>
<p><strong>主从复制功能</strong></p>
<p>虽然数据在内存中读写速度比较快，但是在高并发情况下也会产生读写压力特别大的情况，Redis 针对这一情况提供了主从复制功能。</p>
<p>主从复制的好处有如下两点：</p>
<ul>
<li>提供了 Redis 扩展性，当一台 Redis 不够用时，可以增加多台 Redis 作为从服务器向外提供服务；</li>
<li>提供了<strong>数据备份</strong>和<strong>冗余服务器</strong>，当 Redis 主服务器意外宕机，从服务器可以顶替主服务器向外提供服务，增加了系统的高可用性。</li>
</ul>
<p><strong>脚本操作</strong></p>
<p>Redis 提供了 lua 脚本操作，你可以将 Redis 存取操作写到 lua 脚本里，然后通过 Redis 提供的 API 来执行 lua 脚本，这样就可以实现 Redis 相关操作。</p>
<p>我们同样可以用 Redis 提供的 API 直接实现 Redis 相关操作，那么为什么有时候又要绕一圈去操作 lua 脚本呢？因为 lua 脚本能够保证操作的原子性，即所有的操作当作一个操作，要么全部失败要么全部成功。而直接使用 API 不一定能保证一连串操作的原子性，所以当<strong>需要保证原子性的时候需要使用 lua 脚本</strong>。</p>
<p><strong>发布与订阅</strong></p>
<p>该特性可以将 Redis 作为消息中间件，在服务端产生消息，然后在客户端消费消息队列里的消息，但是作为消息队列不是 Redis 的强项，所以不推荐使用。比如 Redis 作为消息队列消息并非完全可靠，会产生消息丢失的问题，并且也不支持消息分组。在性能上，如果入队和出队操作频繁，那 Redis 性能比起 RabbitMq 等常用消息队列来说还是有差距的。</p>
<p>了解了 Redis 的一些特性，那使用过程中有没有一些注意点呢？其实我们也会踩到坑，比较常见的问题是<strong>缓存穿透</strong>、<strong>缓存击穿</strong>以及<strong>缓存雪崩</strong>，接下来就来讲讲这些问题出现的现象以及如何解决。</p>
<h4>2.Redis 的缺点</h4>
<p><strong>缓存穿透</strong></p>
<p>缓存穿透的情况是 Redis 和 MySQL 数据库都没有这条数据，但是用户不断并发发起请求，请求压力会同时落到数据库和缓存上，这样的情况相对于设计初衷来说，对系统的压力就会大很多了，而且这也是黑客发起攻击的手段之一，找寻你的系统是否存在漏洞。</p>
<p>那在项目中如果遇到缓存穿透我们该如何解决呢？</p>
<p>遇到缓存穿透，我们可以在请求访问缓存和数据库都没查到数据时，给一个默认值或者 Null 值，即 Key-Null。然后该缓存值的有效时间可以设置得短点，比如 30s。在业务代码中判断如果是 Null 值就取消查询数据库，或者间隔 30s 之后重试，这样的方式可以大幅度减轻数据库的查询压力。</p>
<p><strong>缓存击穿</strong></p>
<p>单个数据在缓存中不存在，而在数据库中存在。一般这种情况都是缓存失效导致的，在缓存失效的时间段有大量并发用户访问，首先访问缓存，因为 Key 已经过期了，所以查不到数据，然后所有查询压力都会落到数据库上，造成数据库的压力过大。并且还有可能因为并发问题导致重复更新缓存而过多占用缓存资源。</p>
<p>在项目中如果遇到缓存击穿问题，该如何解决呢？</p>
<ul>
<li>对于一些经常被访问的热点数据，可以根据业务特性主动检查使其 Redis 数据永不过期，当然这样的设置并不代表说这条数据一直不更新而处在 Redis 中，而是根据数据字段中的<strong>失效时间</strong>和<strong>系统时间</strong>的对比主动检查更新数据，使 Redis 数据不会过期；</li>
<li>通过后台定时刷新，根据缓存失效时间节点去批量刷新缓存数据，这个适合 Key 失效时间相对固定的场景。</li>
</ul>
<p><strong>缓存雪崩</strong></p>
<p><strong>大量数据在同一时间失效</strong>，会造成<strong>数据库查询压力过大导致宕机</strong>。缓存雪崩与缓存击穿的区别在于<strong>缓存击穿是单个数据失效</strong>，<strong>缓存雪崩是多个数据同一时间失效</strong>。</p>
<p>在项目中如果遇到缓存雪崩的问题，我们该如何解决呢？以下 3 种方法可以帮我们解决。</p>
<ul>
<li>如果程序设置的缓存过期时间统一为一个固定的值，比如 5s、10s、15s 等等，那么很有可能出现大量数据在同一时间失效。这个时候我们可以设置不同的过期时间，比如统一时间加上一个随机时间，这样可以让缓存的时间尽量均匀分布一点。</li>
<li><strong>不设置过期时间</strong>，让程序的定时任务自动定时更新或者清除缓存</li>
<li><strong>使用集群化的方式</strong>，保证高可用。</li>
</ul>
<h3>总结</h3>
<p>通过本讲的学习你了解了 Redis 的作用，Redis 使用过程中遇到的缓存穿透、缓存击穿以及缓存雪崩现象，及如何解决此类问题，相信你已经有了一个更深刻的认识。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;&#32;如何通过&#32;Arthas&#32;定位代码链路问题？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;如何才能优化&#32;MySQL&#32;性能？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435bb97a2a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E8%AF%B4%E9%80%8F%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
