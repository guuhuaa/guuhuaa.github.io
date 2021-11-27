<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>26 JConsole 与四字母命令：如何监控服务器上 ZooKeeper 的运行状态？.md</title>
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

                    
                    <a href="23&#32;使用&#32;ZooKeeper&#32;实现负载均衡服务器功能.md">23 使用 ZooKeeper 实现负载均衡服务器功能.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;ZooKeeper&#32;在&#32;Kafka&#32;和&#32;Dubbo&#32;中的工业级实现案例分析.md">24 ZooKeeper 在 Kafka 和 Dubbo 中的工业级实现案例分析.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;如何搭建一个高可用的&#32;ZooKeeper&#32;生产环境？.md">25 如何搭建一个高可用的 ZooKeeper 生产环境？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="26&#32;JConsole&#32;与四字母命令：如何监控服务器上&#32;ZooKeeper&#32;的运行状态？.md">26 JConsole 与四字母命令：如何监控服务器上 ZooKeeper 的运行状态？.md</a>
                    

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
                        <div><h1>26 JConsole 与四字母命令：如何监控服务器上 ZooKeeper 的运行状态？</h1>
<p>在上节课中我们学习了在生产环境中，如何部署 ZooKeeper 集群服务。为了我们的程序服务能够持续稳定地对外提供服务，除了在部署的时候尽量采用分布式、集群服务等方式提高 ZooKeeper 服务的可靠性外，在服务上线运行的时候，我们还可以通过对 ZooKeeper 服务的运行状态进行监控，如运行 ZooKeeper 服务的生产服务器的 CPU 、内存、磁盘等使用情况来达到目的。在系统性能达到瓶颈的时候，可以增加服务器资源，以保证服务的稳定性。</p>
<h3>JConsole 介绍</h3>
<p>通常使用 Java 语言进行开发的技术人员对 JConsole 并不陌生。JConsole 是 JDK 自带的工具，用来监控程序运行的状态信息。如下图所示，我们打开系统的控制终端，输入 JConsole 就会弹出一个这样的监控界面。</p>
<p><img src="assets/CgqCHl8kAy2ANt38AADolBOTa2s256.png" alt="image.png" /></p>
<h3>JConsole 使用</h3>
<p>介绍完 JConsole 的基本信息后，接下来我们来了解如何利用 JConsole 对远程 ZooKeeper 集群服务进行监控。之所以能够通过 JConsole 连接 ZooKeeper 服务进行监控，是因为 ZooKeeper 支持 JMX（Java Management Extensions），即 Java 管理扩展，它是一个为应用程序、设备、系统等植入管理功能的框架。</p>
<p>JMX 可以跨越一系列异构操作系统平台、系统体系结构和网络传输协议，灵活地开发无缝集成的系统、网络和服务管理应用。我们可以通过 JMX 来访问和管理 ZooKeeper 服务集群。接下来我们就来介绍一下监控 ZooKeeper 集群服务的相关配置操作。</p>
<p>在 JConsole 配置信息中，连接我们要进行监控的 ZooKeeper 集群服务器。如下面的流程所示，在配置文件中输入 ZooKeeper 服务器的地址端口等相关信息。</p>
<h4>开启 JMX</h4>
<p>首先，我们先开启 ZooKeeper 的 JMX 功能。在 ZooKeeper 安装目录下找到 bin 文件夹，在 bin 文件夹中 ，通过 vim 命令来编辑 zkServer.sh 文件。如下代码所示，输入 JMX 服务的端口号并禁止身份认证等配置。</p>
<pre><code>-Dcom.sun.management.jmxremote.port=50000 

-Dcom.sun.management.jmxremote.ssl=false 

-Dcom.sun.management.jmxremote.authenticate=false 
</code></pre>
<h4>连接 ZooKeeper</h4>
<p>配置完 JMX 的开启功能后，接下来我们通过系统终端启动 JConsole ，再在弹出的对话框中选择远程连接，然后在远程连接的地址中输入要监控的 ZooKeeper 服务器地址，之后就可以通过 JConsole 监控 ZooKeeper 服务器了。</p>
<p><img src="assets/Ciqc1F8kA0CAF9c9AACQw_N29Fg373.png" alt="image" /></p>
<h3>四字母命令</h3>
<p>除了上面介绍的 JConsole 监控控制台之外，ZooKeeper 还提供了一些命令，可使我们更加灵活地统计监控 ZooKeeper 服务的状态信息。 ZooKeeper 提供的这些命令也叫作四字母命令，如它们的名字一样，每一个命令都是由四个字母组成的。如下代码所示，在操作时，我们会打开系统的控制台，并输入相关的命令来查询 ZooKeeper 服务，比如我们可以输入 stat 命令来查看数据节点等信息。</p>
<pre><code>echo {command} | nc 127.0.0.1 2181 
</code></pre>
<p>介绍完四字母命令的调用方式和执行格式后，接下来我们介绍几种常见的四字母命令，分别是 stat 、srvr，以及 cons 等。</p>
<h4>stat</h4>
<p>stat 命令的作用是监控 ZooKeeper 服务器的状态，我们通过 stat 命令统计 ZooKeeper 服务器的 ZooKeeper 版本信息、集群数节点等信息，如下面的代码所示，我们在操作时会输入 echo stat 命令来输出查询到的服务状态信息到控制台。</p>
<pre><code>$ echo stat | nc localhost 2181 

Zookeeper version: 3.4.13- built on 06/29/2018 04:05 GMT 

Clients: 

 /0:0:0:0:0:0:0:1:40598[0](queued=0,recved=1,sent=0) 

Latency min/avg/max: 0/0/0 

Received: 17 

Sent: 16 

Connections: 1 

Outstanding: 0 

Zxid: 0x0 

Mode: follower 

Node count: 4 
</code></pre>
<h4>srvr</h4>
<p>srvr 命令与 stat 命令的功能十分相似，唯一不同的地方是 srvr 命令不会将与客户端的连接情况输出，通过 srvr 命令只会查询服务器的自身信息。</p>
<pre><code>$ echo srvr | nc localhost 2181 

Zookeeper version: 3.4.13- built on 06/29/2018 04:05 GMT 

Latency min/avg/max: 0/0/0 

Received: 26 

Sent: 25 

Connections: 1 

Outstanding: 0 

Zxid: 0x0 

Mode: follower 

Node count: 4 
</code></pre>
<h4>cons</h4>
<p>cons 命令用于输出当前这台服务器上所有客户端连接的详细信息，包括每个客户端的客户端 IP 、会话 ID 和最后一次与服务器交互的操作类型等。</p>
<pre><code>$ echo cons | nc localhost 2181 

 /0:0:0:0:0:0:0:1:31569[0](queued=0,recved=1,sent=0) 
</code></pre>
<h4>ruok</h4>
<p>ruok 命令的主要作用是查询 ZooKeeper 服务器是否正常运行。如果 ZooKeeper 服务器正常运行，执行完 ruok 命令后，会得到 “imok” 返回值。如果 ZooKeeper 服务没有正常运行，则不会有任何返回值。在使用 ruok 命令的时候，在这里我们要注意的一点是，有些时候即使返回了 “imok” 字段，ZooKeeper 服务也可能没有正常运行，唯一能确定的是该台服务器的 2181 端口是打开的，如下代码所示。</p>
<pre><code>$ echo ruok | nc localhost 2181 
</code></pre>
<h3>监控集群信息</h3>
<p>介绍完系统监控工具 JConsole 以及常用的命令后，接下来我们就从实际的生产角度出发，来看一下在 ZooKeeper 集群生产环境中如何监控系统集群运行情况，以及如何利用我们监控的数据诊断 ZooKeeper 服务的运行问题并解决问题。</p>
<p>虽然 ZooKeeper 服务提供了丰富的四字母命令，让我们可以通过命令来获得 ZooKeeper 服务相关的运行信息，但是在实际的生产环境中， ZooKeeper 集群的规模可能很大，逐一通过命令的方式监控 ZooKeeper 服务显然不可行。因此，这里我们会介绍一种自动的监控 ZooKeeper 集群运行服务的方式。</p>
<p>为了编写自动化监控 ZooKeeper 集群服务，首先我们要明确需要监控哪些数据类型，在这里我们主要对最小会话超时、最大会话超时、最大连接数、发送的数据包、接收的数据包进行监控，而具体的我们则会通过 Zabbix 来实现。</p>
<h4>Zabbix</h4>
<p>Zabbix 是一个性能监控的管理工具，它基于 Web 界面提供分布式系统监视，以及网络监视功能的企业级开源解决方案。</p>
<h4>安装</h4>
<p>我们可以通过 Maven 或 Gradle 项目管理工具下载 Zabbix，这里我们主要以 Maven 工程为例，如下代码所示，需要在 pom 文件中引入相关的配置信息。</p>
<pre><code>&lt;dependency&gt; 

    &lt;groupId&gt;io.github.cgi&lt;/groupId&gt; 

    &lt;artifactId&gt;zabbix-api&lt;/artifactId&gt; 

    &lt;version&gt;0.0.5&lt;/version&gt; 

&lt;/dependency&gt; 
</code></pre>
<h4>配置项</h4>
<p>将 Zabbix 引入到我们的工程项目后，接下来，就可以编写一个程序来自动化地获取 ZooKeeper 服务的相关信息。这里我们创建一个 ZooKeeperInfo 脚本，如下代码所示，在脚本文件中我们创建了一个 mntr 数组变量用来设置我们想要监控的服务参数，比如 minSessionTimeout 最小超时时间、maxSessionTimeout 最大超时时间等。</p>
<pre><code>public class ZooKeepInfo(){ 

	Static Final String ZookeeperServer = '127.0.0.1' 

	Static Final String ZookeeperPort = 2181 

	Static Final String ZookeeperCommand = 'mntr' 

	Static Final String ZookeeperKey = 'zk_version 

	 

	CommandKey={ 

	'conf':['clientPort','dataDir','dataLogDir','tickTime','maxClientCnxns','minSessionTimeout','maxSessionTimeout','serverId','initLimit','syncLimit','electionAlg','electionPort','quorumPort','peerType'], 

	'ruok':['state'], 

	'mntr':['zk_version','zk_avg_latency','zk_max_latency','zk_min_latency','zk_packets_received','zk_packets_sent','zk_num_alive_connections','zk_outstanding_requests','zk_server_state','zk_znode_count','zk_watch_count','zk_ephemerals_count','zk_approximate_data_size','zk_open_file_descriptor_count','zk_max_file_descriptor_count','zk_followers','zk_synced_followers','zk_pending_syncs'] 

	} 

	 

	class ZooKeeperCommands(object): 

	    def ZooKeeperCommands(self,server,port,zkCommand,zkKey): 

	        self._server = server 

	        self._port = port 

	        self._zkCommand = zkCommand 

	        self._zkKey = zkKey 

	        self._value_raw = None 

	        self._value = None  

	 

	    void zkExec(this): 

	        self._exec_command() 

	        self._parse_value() 

	        return self._value 

	     

	    void _exec_command(this): 

	        Telnet tn = Telnet(self._server, self._port, timeout=30) 

	        tn.read_until('login: ') 

	        tn.write(username + '\n') 

	        tn.read_until('password: ') 

	        tn.write(password + '\n') 

	        tn.read_until(finish) 

	} 
</code></pre>
<h3>结束</h3>
<p>本节课我们主要学习了 ZooKeeper 集群在日常生产环境中的维护问题。首先介绍了 ZooKeeper 集群通过 JMX 方式进行远程监控的方法，然后学习了 JConsole 以及四字母命令的使用方式，最后介绍了在实际工作中，面对大规模的 ZooKeeper 集群时，我们如何做到自动化的获取监控数据。</p>
<p>本节课在实现自动化的数据获取时，利用了一个开源的性能监控工具 Zabbix 。除了课中提到的一些性能监控参数外，我们也可以利用 Zabbix 监控一些和自身业务相关的数据信息，比如在对数据节点的创建数量有严格要求的情况下，我们可以编写相关的脚本对某一个数据节点下子节点的创建个数进行监控，当该子节点个数大于我们设置的某一个临界值时，会给出报警或禁止该节点再进行创建操作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="25&#32;如何搭建一个高可用的&#32;ZooKeeper&#32;生产环境？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="27&#32;crontab&#32;与&#32;PurgeTxnLog：线上系统日志清理的最佳时间和方式.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434f1a9f2570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
