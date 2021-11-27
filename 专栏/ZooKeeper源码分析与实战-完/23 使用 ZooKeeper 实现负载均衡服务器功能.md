<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23 使用 ZooKeeper 实现负载均衡服务器功能.md</title>
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

                    
                    <a href="00&#32;开篇词：选择&#32;ZooKeeper，一步到位掌握分布式开发.md">00 开篇词：选择 ZooKeeper，一步到位掌握分布式开发.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;ZooKeeper&#32;数据模型：节点的特性与应用.md">01 ZooKeeper 数据模型：节点的特性与应用.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;发布订阅模式：如何使用&#32;Watch&#32;机制实现分布式通知.md">02 发布订阅模式：如何使用 Watch 机制实现分布式通知.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;ACL&#32;权限控制：如何避免未经授权的访问？.md">03 ACL 权限控制：如何避免未经授权的访问？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;ZooKeeper&#32;如何进行序列化？.md">04 ZooKeeper 如何进行序列化？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;深入分析&#32;Jute&#32;的底层实现原理.md">05 深入分析 Jute 的底层实现原理.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;ZooKeeper&#32;的网络通信协议详解.md">06 ZooKeeper 的网络通信协议详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;单机模式：服务器如何从初始化到对外提供服务？.md">07 单机模式：服务器如何从初始化到对外提供服务？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;集群模式：服务器如何从初始化到对外提供服务？.md">08 集群模式：服务器如何从初始化到对外提供服务？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;创建会话：避开日常开发的那些“坑”.md">09 创建会话：避开日常开发的那些“坑”.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;ClientCnxn：客户端核心工作类工作原理解析.md">10 ClientCnxn：客户端核心工作类工作原理解析.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;分桶策略：如何实现高效的会话管理？.md">11 分桶策略：如何实现高效的会话管理？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;服务端是如何处理一次会话请求的？.md">12 服务端是如何处理一次会话请求的？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;Curator：如何降低&#32;ZooKeeper&#32;使用的复杂性？.md">13 Curator：如何降低 ZooKeeper 使用的复杂性？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;Leader&#32;选举：如何保证分布式数据的一致性？.md">14 Leader 选举：如何保证分布式数据的一致性？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;ZooKeeper&#32;究竟是怎么选中&#32;Leader&#32;的？.md">15 ZooKeeper 究竟是怎么选中 Leader 的？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;ZooKeeper&#32;集群中&#32;Leader&#32;与&#32;Follower&#32;的数据同步策略.md">16 ZooKeeper 集群中 Leader 与 Follower 的数据同步策略.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;集群中&#32;Leader&#32;的作用：事务的请求处理与调度分析.md">17 集群中 Leader 的作用：事务的请求处理与调度分析.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;集群中&#32;Follow&#32;的作用：非事务请求的处理与&#32;Leader&#32;的选举分析.md">18 集群中 Follow 的作用：非事务请求的处理与 Leader 的选举分析.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Observer&#32;的作用与&#32;Follow&#32;有哪些不同？.md">19 Observer 的作用与 Follow 有哪些不同？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;一个运行中的&#32;ZooKeeper&#32;服务会产生哪些数据和文件？.md">20 一个运行中的 ZooKeeper 服务会产生哪些数据和文件？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;ZooKeeper&#32;分布式锁：实现和原理解析.md">21 ZooKeeper 分布式锁：实现和原理解析.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;基于&#32;ZooKeeper&#32;命名服务的应用：分布式&#32;ID&#32;生成器.md">22 基于 ZooKeeper 命名服务的应用：分布式 ID 生成器.md</a>

                </li>
                <li>

                    <a class="current-tab" href="23&#32;使用&#32;ZooKeeper&#32;实现负载均衡服务器功能.md">23 使用 ZooKeeper 实现负载均衡服务器功能.md</a>
                    

                </li>
                <li>

                    
                    <a href="24&#32;ZooKeeper&#32;在&#32;Kafka&#32;和&#32;Dubbo&#32;中的工业级实现案例分析.md">24 ZooKeeper 在 Kafka 和 Dubbo 中的工业级实现案例分析.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;如何搭建一个高可用的&#32;ZooKeeper&#32;生产环境？.md">25 如何搭建一个高可用的 ZooKeeper 生产环境？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;JConsole&#32;与四字母命令：如何监控服务器上&#32;ZooKeeper&#32;的运行状态？.md">26 JConsole 与四字母命令：如何监控服务器上 ZooKeeper 的运行状态？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;crontab&#32;与&#32;PurgeTxnLog：线上系统日志清理的最佳时间和方式.md">27 crontab 与 PurgeTxnLog：线上系统日志清理的最佳时间和方式.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;彻底掌握二阶段提交三阶段提交算法原理.md">28 彻底掌握二阶段提交三阶段提交算法原理.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;ZAB&#32;协议算法：崩溃恢复和消息广播.md">29 ZAB 协议算法：崩溃恢复和消息广播.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;ZAB&#32;与&#32;Paxos&#32;算法的联系与区别.md">30 ZAB 与 Paxos 算法的联系与区别.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;ZooKeeper&#32;中二阶段提交算法的实现分析.md">31 ZooKeeper 中二阶段提交算法的实现分析.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;ZooKeeper&#32;数据存储底层实现解析.md">32 ZooKeeper 数据存储底层实现解析.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;结束语&#32;&#32;分布技术发展与&#32;ZooKeeper&#32;应用前景.md">33 结束语  分布技术发展与 ZooKeeper 应用前景.md</a>

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
                        <div><h1>23 使用 ZooKeeper 实现负载均衡服务器功能</h1>
<p>今天我们利用 ZooKeeper 的相关知识，学习如何解决分布式环境下常见的业务场景与需求。这个课时主要通过 ZooKeeper 的相关特性，实现一个负载均衡服务器。在分布式架构和集群服务器架构下，负载均衡可以提高网络的性能和可靠性。</p>
<h3>什么是负载均衡</h3>
<p>负载均衡可以理解为运行在网络中的服务器或软件，其主要作用是<strong>扩展网络服务器的带宽、提高服务器处理数据的吞吐量，提高网络的可用性</strong>。比如我们经常用到的网络服务器、邮件服务器以及很多商业系统的服务器，都采用负载均衡的方式来协调工作。</p>
<p>这些系统一般会采用集群的方式进行部署，由于这些服务器彼此所处的网络环境各不相同，在某一段时间内所接收并处理的数据有多有少，如果整个集群没有一个专门进行管理和协调的角色，随着网络请求越来越多，就会出现某一台服务器比较忙，而网络中其他服务器没有什么任务要处理的情况。</p>
<p>负载均衡通过监控网络中各个服务器的运行情况，对整个集群的计算资源进行合理地分配和调整，避免由于请求处理的无序性导致的短板，从而限制整个集群性能。</p>
<p>了解了负载均衡服务器在集群服务中的作用后，接下来再来介绍一下实现负载均衡的常用算法。</p>
<h3>负载均衡算法</h3>
<p>在我们平时的工作和面试中，也常被问及一些负载均衡的算法问题。常用的有轮询法、随机法、原地址哈希法、加权轮询法、加权随机法、最小连接数法，下面我来分别为你进行讲解。</p>
<h4>轮询法</h4>
<p>轮询法是最为简单的负载均衡算法，当接收到来自网络中的客户端请求后，负载均衡服务器会按顺序逐个分配给后端服务。比如集群中有 3 台服务器，分别是 server1、server2、server3，轮询法会按照 sever1、server2、server3 这个顺序依次分发会话请求给每个服务器。当第一次轮询结束后，会重新开始下一轮的循环。</p>
<h4>随机法</h4>
<p>随机算法是指负载均衡服务器在接收到来自客户端的请求后，会根据一定的随机算法选中后台集群中的一台服务器来处理这次会话请求。不过，当集群中备选机器变的越来越多时，通过统计学我们可以知道每台机器被抽中的概率基本相等，因此随机算法的实际效果越来越趋近轮询算法。</p>
<h4>原地址哈希法</h4>
<p>原地址哈希算法的核心思想是根据客户端的 IP 地址进行哈希计算，用计算结果进行取模后，根据最终结果选择服务器地址列表中的一台机器，处理该条会话请求。采用这种算法后，当同一 IP 的客户端再次访问服务端后，负载均衡服务器最终选举的还是上次处理该台机器会话请求的服务器，<strong>也就是每次都会分配同一台服务器给客户端</strong>。</p>
<h4>加权轮询法</h4>
<p>在实际的生成环境中，一个分布式或集群系统中的机器可能部署在不同的网络环境中，每台机器的配置性能也有优劣之分。因此，它们处理和响应客户端请求的能力也各不相同。采用上面几种负载均衡算法，都不太合适，这会造成能力强的服务器在处理完业务后过早进入限制状态，而性能差或网络环境不好的服务器，一直忙于处理请求，造成任务积压。</p>
<p>为了解决这个问题，我们可以采用加权轮询法，加权轮询的方式与轮询算法的方式很相似，唯一的不同在于选择机器的时候，不只是单纯按照顺序的方式选择，<strong>还根据机器的配置和性能高低有所侧重</strong>，配置性能好的机器往往首先分配。</p>
<h4>加权随机法</h4>
<p>加权随机法和我们上面提到的随机算法一样，在采用随机算法选举服务器的时候，会考虑系统性能作为权值条件。</p>
<h4>最小连接数法</h4>
<p>最小连接数算法是指，根据后台处理客户端的连接会话条数，计算应该把新会话分配给哪一台服务器。一般认为，连接数越少的机器，在网络带宽和计算性能上都有很大优势，会作为最优先分配的对象。</p>
<h3>利用 ZooKeeper 实现</h3>
<p>介绍完负载均衡的常用算法后，接下来我们利用 ZooKeeper 来实现一个分布式系统下的负载均衡服务器。从上面介绍的几种负载均衡算法中不难看出。一个负载均衡服务器的底层实现，<strong>关键在于找到网络集群中最适合处理该条会话请求的机器，并将该条会话请求分配给该台机器</strong>。因此探测和发现后台服务器的运行状态变得最为关键。</p>
<h4>状态收集</h4>
<p>首先我们来实现网络中服务器运行状态的收集功能，利用 ZooKeeper 中的临时节点作为标记网络中服务器的状态点位。在网络中服务器上线运行的时候，通过在 ZooKeeper 服务器中创建临时节点，向 ZooKeeper 的服务列表进行注册，表示本台服务器已经上线可以正常工作。通过删除临时节点或者在与 ZooKeeper 服务器断开连接后，删除该临时节点。</p>
<p>最后，通过统计临时节点的数量，来了解网络中服务器的运行情况。<strong>如下图所示，建立的 ZooKeeper 数据模型中 Severs 节点可以作为存储服务器列表的父节点</strong>。用于之后通过负载均衡算法在该列表中选择服务器。在它下面创建 servers_host1、servers_host2、servers_host3等临时节点来存储集群中的服务器运行状态信息。</p>
<p><img src="assets/Ciqc1F8X5l-APWIjAAAsDI_4m_Q833.png" alt="Drawing 0.png" /></p>
<p>在代码层面的实现中，我们首先定义一个 BlanceSever 接口类。该类规定在 ZooKeeper 服务器启动后，向服务器地址列表中，注册或注销信息以及根据接收到的会话请求，动态更新负载均衡情况等功能。如下面的代码所示：</p>
<pre><code>public class BlanceSever{

  public void register()

  public void unregister()

  public void addBlanceCount()

  public void takeBlanceCount()

  

}
</code></pre>
<p>之后我们创建 BlanceSever 接口的实现类 BlanceSeverImpl，在 BlanceSeverImpl 类中首先定义服务器运行的 Session 超时时间、会话连接超时时间、ZooKeeper 客户端地址、服务器地址列表节点 ‘/Severs’ 等基本参数。并通过构造函数，在类被引用时进行初始化 ZooKeeper 客户端对象实例。</p>
<pre><code>public class BlanceSeverImpl implements BlanceSever{

  private static final Integer SESSION_TIME_OUT

  private static final Integer CONNECTION_TIME_OUT

  private final ZkClient zkclient

  private static final SERVER_PATH=&quot;/Severs&quot;

  public BlanceSeverImpl(){

    init...

  }

  

}
</code></pre>
<p>接下来，在定义当服务器启动时，向服务器地址列表注册信息的 register 函数。在函数的内部，通过在 SERVER_PATH 路径下创建临时子节点的方式来注册服务器信息。如下面的代码所示，首先获取服务器的 ip 地址，利用 ip 地址作为临时节点的 path 来创建临时节点。</p>
<pre><code>public register() throws Exception{

  InetAddress address = InetAddress.getLocalHost();

  String serverIp=address.getHostAddress()

  zkclient.createEphemeral(SERVER_PATH+serverIp)

}
</code></pre>
<p>register 函数在服务器启动并注册服务器信息后，我们再来定义 unregister 方法，该方法是当服务器关机或由于其他原因不再对外提供服务时，通过调用 unregister 方法，注销该台服务器在服务器列表中的信息。</p>
<p>注销后的机器不会被负载均衡服务器分发处理会话。如下面的代码所示，在 unregister 函数的内部，我们主要通过删除 SERVER_PATH 路径下临时节点的方式注销服务器。</p>
<pre><code>public unregister() throws Exception{

  zkclient.delete(SERVER_PATH+serverIp)

}
</code></pre>
<h4>负载算法</h4>
<p>实现服务器列表后，接下来我们就进入负载均衡最核心的内容：如何选择服务器。这里我们通过采用“最小连接数”算法，来确定究竟如何均衡地分配网络会话请求给后台客户端。</p>
<p>整个实现的过程如下图所示。首先，在接收到客户端的请求后，通过 getData 方法获取服务端 Severs 节点下的服务器列表，其中每个节点信息都存储有当前服务器的连接数。通过判断选择最少的连接数作为当前会话的处理服务器，并通过 setData 方法将该节点连接数加 1。最后，当客户端执行完毕，再调用 setData 方法将该节点信息减 1。</p>
<p><img src="assets/Ciqc1F8X5n6AGCBQAABSbLOIuWA010.png" alt="Drawing 1.png" /></p>
<p>首先，我们定义当服务器接收到会话请求后。在 ZooKeeper 服务端增加连接数的 addBlance 方法。如下面的代码所示，首先我们通过 readData 方法获取服务器最新的连接数，之后将该连接数加 1，再通过 writeData 方法将新的连接数信息写入到服务端对应节点信息中。</p>
<pre><code>public void addBlance() throws Exception{

  InetAddress address = InetAddress.getLocalHost();

  String serverIp=address.getHostAddress()

  Integer con_count=zkClient.readData(SERVER_PATH+serverIp)

  ++con_count

  zkClient.writeData(SERVER_PATH+serverIp,con_count)

}
</code></pre>
<p>当服务器处理完该会话请求后，需要更新服务端相关节点的连接数。具体的操作与 addBlance 方法基本一样，只是对获取的连接信息进行减一操作，这里不再赘述。</p>
<h3>结束</h3>
<p>本课时我们介绍了如何利用 ZooKeeper 实现一个负载均衡服务器，了解了随机、轮询、哈希等常用的负载均衡算法，并在本课的结尾利用 ZooKeeper 来创建一个负载均衡服务器的具体实现过程。</p>
<p>这里请你注意：我们日常用到的负载均衡器主要是选择后台处理的服务器，并给其分发请求。而通过 ZooKeeper 实现的服务器，只提供了服务器的筛选工作。在请求分发的过程中，还是通过负载算法计算出要访问的服务器，之后客户端自己连接该服务器，完成请求操作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;基于&#32;ZooKeeper&#32;命名服务的应用：分布式&#32;ID&#32;生成器.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;ZooKeeper&#32;在&#32;Kafka&#32;和&#32;Dubbo&#32;中的工业级实现案例分析.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434f0aeed470ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ZooKeeper%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
