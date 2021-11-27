<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03 安装：ElasticSearch和Kibana安装.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>

                </li>
                <li>

                    <a class="current-tab" href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>
                    

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>03 安装：ElasticSearch和Kibana安装</h1>
<h2>安装ElasticSearch</h2>
<blockquote>
<p>ElasticSearch 是基于Java平台的，所以先要安装Java</p>
</blockquote>
<ul>
<li><strong>平台确认</strong></li>
</ul>
<p>这里我准备了一台Centos7虚拟机, 为方便选择后续安装的版本，所以需要看下系统版本信息。</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="65170a0a1125332848554854514806000b110a16">[email&#160;protected]</a> ~]# uname -a
Linux VM-0-14-centos 3.10.0-862.el7.x86_64 #1 SMP Fri Apr 20 16:44:24 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
    
</code></pre>
<ul>
<li><strong>安装Java</strong></li>
</ul>
<p>安装 Elasticsearch 之前，你需要先安装一个较新的版本的 Java，最好的选择是，你可以从 <a href="https://www.java.com">www.java.com  </a> 获得官方提供的最新版本的 Java。安装以后，确认是否安装成功：</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="067469697246504b2b362b37322b656368726975">[email&#160;protected]</a> ~]# java --version
openjdk 14.0.2 2020-07-14
OpenJDK Runtime Environment 20.3 (slowdebug build 14.0.2+12)
OpenJDK 64-Bit Server VM 20.3 (slowdebug build 14.0.2+12, mixed mode, sharing)
    
</code></pre>
<ul>
<li><strong>下载ElasticSearch</strong></li>
</ul>
<p>从<a href="https://www.elastic.co/cn/downloads/elasticsearch">这里  </a>下载ElasticSearch</p>
<p>比如可以通过curl下载</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="10627f7f6450465d3d203d21243d73757e647f63">[email&#160;protected]</a> opt]# curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.12.0-linux-x86_64.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
    
</code></pre>
<ul>
<li><strong>解压</strong></li>
</ul>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e1938e8e95a1b7acccd1ccd0d5cc82848f958e92">[email&#160;protected]</a> opt]# tar zxvf /opt/elasticsearch-7.12.0-linux-x86_64.tar.gz 
...
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="067469697246504b2b362b37322b656368726975">[email&#160;protected]</a> opt]# ll | grep elasticsearch
drwxr-xr-x  9 root root      4096 Mar 18 14:21 elasticsearch-7.12.0
-rw-r--r--  1 root root 327497331 Apr  5 21:05 elasticsearch-7.12.0-linux-x86_64.tar.gz
    
</code></pre>
<ul>
<li><strong>增加elasticSearch用户</strong></li>
</ul>
<p>必须创建一个非root用户来运行ElasticSearch(ElasticSearch5及以上版本，基于安全考虑，强制规定不能以root身份运行。)</p>
<p>如果你使用root用户来启动ElasticSearch，则会有如下错误信息：</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="275548485367716a0a170a16130a444249534854">[email&#160;protected]</a> opt]# cd elasticsearch-7.12.0/
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="aedcc1c1daeef8e3839e839f9a83cdcbc0dac1dd">[email&#160;protected]</a> elasticsearch-7.12.0]# ./bin/elasticsearch
[2021-04-05T21:36:46,510][ERROR][o.e.b.ElasticsearchUncaughtExceptionHandler] [VM-0-14-centos] uncaught exception in thread [main]
org.elasticsearch.bootstrap.StartupException: java.lang.RuntimeException: can not run elasticsearch as root
        at org.elasticsearch.bootstrap.Elasticsearch.init(Elasticsearch.java:163) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.bootstrap.Elasticsearch.execute(Elasticsearch.java:150) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.cli.EnvironmentAwareCommand.execute(EnvironmentAwareCommand.java:75) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.cli.Command.mainWithoutErrorHandling(Command.java:116) ~[elasticsearch-cli-7.12.0.jar:7.12.0]
        at org.elasticsearch.cli.Command.main(Command.java:79) ~[elasticsearch-cli-7.12.0.jar:7.12.0]
        at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:115) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:81) ~[elasticsearch-7.12.0.jar:7.12.0]
Caused by: java.lang.RuntimeException: can not run elasticsearch as root
        at org.elasticsearch.bootstrap.Bootstrap.initializeNatives(Bootstrap.java:101) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.bootstrap.Bootstrap.setup(Bootstrap.java:168) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.bootstrap.Bootstrap.init(Bootstrap.java:397) ~[elasticsearch-7.12.0.jar:7.12.0]
        at org.elasticsearch.bootstrap.Elasticsearch.init(Elasticsearch.java:159) ~[elasticsearch-7.12.0.jar:7.12.0]
        ... 6 more
uncaught exception in thread [main]
java.lang.RuntimeException: can not run elasticsearch as root
        at org.elasticsearch.bootstrap.Bootstrap.initializeNatives(Bootstrap.java:101)
        at org.elasticsearch.bootstrap.Bootstrap.setup(Bootstrap.java:168)
        at org.elasticsearch.bootstrap.Bootstrap.init(Bootstrap.java:397)
        at org.elasticsearch.bootstrap.Elasticsearch.init(Elasticsearch.java:159)
        at org.elasticsearch.bootstrap.Elasticsearch.execute(Elasticsearch.java:150)
        at org.elasticsearch.cli.EnvironmentAwareCommand.execute(EnvironmentAwareCommand.java:75)
        at org.elasticsearch.cli.Command.mainWithoutErrorHandling(Command.java:116)
        at org.elasticsearch.cli.Command.main(Command.java:79)
        at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:115)
        at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:81)
For complete error details, refer to the log at /opt/elasticsearch-7.12.0/logs/elasticsearch.log
2021-04-05 13:36:46,979269 UTC [8846] INFO  <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c08da1a9aeeea3a380f1f0f6">[email&#160;protected]</a> Parent process died - ML controller exiting
    
</code></pre>
<p>所以我们增加一个独立的elasticsearch用户来运行</p>
<pre><code class="language-bash"># 增加elasticsearch用户
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="0e7c61617a4e5843233e233f3a236d6b607a617d">[email&#160;protected]</a> elasticsearch-7.12.0]# useradd elasticsearch
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="6a1805051e2a3c27475a475b5e47090f041e0519">[email&#160;protected]</a> elasticsearch-7.12.0]# passwd elasticsearch
Changing password for user elasticsearch.
New password: 
BAD PASSWORD: The password contains the user name in some form
Retype new password: 
passwd: all authentication tokens updated successfully.

# 修改目录权限至新增的elasticsearch用户
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="01736e6e7541574c2c312c30352c62646f756e72">[email&#160;protected]</a> elasticsearch-7.12.0]# chown -R elasticsearch /opt/elasticsearch-7.12.0
# 增加data和log存放区，并赋予elasticsearch用户权限
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4f3d20203b0f1902627f627e7b622c2a213b203c">[email&#160;protected]</a> elasticsearch-7.12.0]# mkdir -p /data/es
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fb8994948fbbadb6d6cbd6cacfd6989e958f9488">[email&#160;protected]</a> elasticsearch-7.12.0]# chown -R elasticsearch /data/es
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="15677a7a6155435838253824213876707b617a66">[email&#160;protected]</a> elasticsearch-7.12.0]# mkdir -p /var/log/es
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="11637e7e6551475c3c213c20253c72747f657e62">[email&#160;protected]</a> elasticsearch-7.12.0]# chown -R elasticsearch /var/log/es

    
</code></pre>
<p>然后修改上述的data和log路径，<code>vi /opt/elasticsearch-7.12.0/config/elasticsearch.yml</code></p>
<pre><code class="language-bash"># ----------------------------------- Paths ------------------------------------
#
# Path to directory where to store the data (separate multiple locations by comma):
#
path.data: /data/es
#
# Path to log files:
#
path.logs: /var/log/es
    
</code></pre>
<ul>
<li><strong>修改Linux系统的限制配置</strong></li>
</ul>
<ol>
<li>修改系统中允许应用最多创建多少文件等的限制权限。Linux默认来说，一般限制应用最多创建的文件是65535个。但是ES至少需要65536的文件创建权限。</li>
<li>修改系统中允许用户启动的进程开启多少个线程。默认的Linux限制root用户开启的进程可以开启任意数量的线程，其他用户开启的进程可以开启1024个线程。必须修改限制数为4096+。因为ES至少需要4096的线程池预备。ES在5.x版本之后，强制要求在linux中不能使用root用户启动ES进程。所以必须使用其他用户启动ES进程才可以。</li>
<li>Linux低版本内核为线程分配的内存是128K。4.x版本的内核分配的内存更大。如果虚拟机的内存是1G，最多只能开启3000+个线程数。至少为虚拟机分配1.5G以上的内存。</li>
</ol>
<p>修改如下配置</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1c6e7373685c4a51312c312d28317f797268736f">[email&#160;protected]</a> elasticsearch-7.12.0]# vi /etc/security/limits.conf

elasticsearch soft nofile 65536
elasticsearch hard nofile 65536
elasticsearch soft nproc 4096
elasticsearch hard nproc 4096
    
</code></pre>
<ul>
<li><strong>启动ElasticSearch</strong></li>
</ul>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="85f7eaeaf1c5d3c8a8b5a8b4b1a8e6e0ebf1eaf6">[email&#160;protected]</a> elasticsearch-7.12.0]# su elasticsearch
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="06636a6775726f6575636774656e46504b2b362b37322b656368726975">[email&#160;protected]</a> elasticsearch-7.12.0]$ ./bin/elasticsearch -d
[2021-04-05T22:03:38,332][INFO ][o.e.n.Node               ] [VM-0-14-centos] version[7.12.0], pid[13197], build[default/tar/78722783c38caa25a70982b5b042074cde5d3b3a/2021-03-18T06:17:15.410153305Z], OS[Linux/3.10.0-862.el7.x86_64/amd64], JVM[AdoptOpenJDK/OpenJDK 64-Bit Server VM/15.0.1/15.0.1+9]
[2021-04-05T22:03:38,348][INFO ][o.e.n.Node               ] [VM-0-14-centos] JVM home [/opt/elasticsearch-7.12.0/jdk], using bundled JDK [true]
[2021-04-05T22:03:38,348][INFO ][o.e.n.Node               ] [VM-0-14-centos] JVM arguments [-Xshare:auto, -Des.networkaddress.cache.ttl=60, -Des.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -XX:+ShowCodeDetailsInExceptionMessages, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dio.netty.allocator.numDirectArenas=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Djava.locale.providers=SPI,COMPAT, --add-opens=java.base/java.io=ALL-UNNAMED, -XX:+UseG1GC, -Djava.io.tmpdir=/tmp/elasticsearch-17264135248464897093, -XX:+HeapDumpOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Xms1894m, -Xmx1894m, -XX:MaxDirectMemorySize=993001472, -XX:G1HeapRegionSize=4m, -XX:InitiatingHeapOccupancyPercent=30, -XX:G1ReservePercent=15, -Des.path.home=/opt/elasticsearch-7.12.0, -Des.path.conf=/opt/elasticsearch-7.12.0/config, -Des.distribution.flavor=default, -Des.distribution.type=tar, -Des.bundled_jdk=true]
    
</code></pre>
<ul>
<li><strong>查看安装是否成功</strong></li>
</ul>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c0b2afafb480968dedf0edf1f4eda3a5aeb4afb3">[email&#160;protected]</a> ~]# netstat -ntlp | grep 9200
tcp6       0      0 127.0.0.1:9200          :::*                    LISTEN      13549/java          
tcp6       0      0 ::1:9200                :::*                    LISTEN      13549/java          
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d0a2bfbfa490869dfde0fde1e4fdb3b5bea4bfa3">[email&#160;protected]</a> ~]# curl 127.0.0.1:9200
{
  &quot;name&quot; : &quot;VM-0-14-centos&quot;,
  &quot;cluster_name&quot; : &quot;elasticsearch&quot;,
  &quot;cluster_uuid&quot; : &quot;ihttW8b2TfWSkwf_YgPH2Q&quot;,
  &quot;version&quot; : {
    &quot;number&quot; : &quot;7.12.0&quot;,
    &quot;build_flavor&quot; : &quot;default&quot;,
    &quot;build_type&quot; : &quot;tar&quot;,
    &quot;build_hash&quot; : &quot;78722783c38caa25a70982b5b042074cde5d3b3a&quot;,
    &quot;build_date&quot; : &quot;2021-03-18T06:17:15.410153305Z&quot;,
    &quot;build_snapshot&quot; : false,
    &quot;lucene_version&quot; : &quot;8.8.0&quot;,
    &quot;minimum_wire_compatibility_version&quot; : &quot;6.8.0&quot;,
    &quot;minimum_index_compatibility_version&quot; : &quot;6.0.0-beta1&quot;
  },
  &quot;tagline&quot; : &quot;You Know, for Search&quot;
}
    
</code></pre>
<h2>安装Kibana</h2>
<blockquote>
<p>Kibana是界面化的查询数据的工具，下载时尽量下载与ElasicSearch一致的版本。</p>
</blockquote>
<ul>
<li><strong>下载Kibana</strong></li>
</ul>
<p>从<a href="https://www.elastic.co/cn/downloads/kibana">这里  </a>下载Kibana</p>
<ul>
<li><strong>解压</strong></li>
</ul>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2b5944445f6b7d66061b061a1f06484e455f4458">[email&#160;protected]</a> opt]# tar -vxzf kibana-7.12.0-linux-x86_64.tar.gz
    
</code></pre>
<ul>
<li><strong>使用elasticsearch用户权限</strong></li>
</ul>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d7a5b8b8a397819afae7fae6e3fab4b2b9a3b8a4">[email&#160;protected]</a> opt]# chown -R elasticsearch /opt/kibana-7.12.0-linux-x86_64
#配置Kibana的远程访问
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d0a2bfbfa490869dfde0fde1e4fdb3b5bea4bfa3">[email&#160;protected]</a> opt]# vi /opt/kibana-7.12.0-linux-x86_64/config/kibana.yml
server.host: 0.0.0.0
    
</code></pre>
<ul>
<li><strong>启动</strong></li>
</ul>
<p>需要切换至elasticsearch用户</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3a4855554e7a6c77170a170b0e17595f544e5549">[email&#160;protected]</a> opt]# su elasticsearch
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="dbbeb7baa8afb2b8a8bebaa9b8b39b8d96f6ebf6eaeff6b8beb5afb4a8">[email&#160;protected]</a> opt]$ cd /opt/kibana-7.12.0-linux-x86_64/
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ec89808d9f98858f9f898d9e8f84acbaa1c1dcc1ddd8c18f898298839f">[email&#160;protected]</a> kibana-7.12.0-linux-x86_64]$ ./bin/kibana
  log   [22:30:22.185] [info][plugins-service] Plugin &quot;osquery&quot; is disabled.
  log   [22:30:22.283] [warning][config][deprecation] Config key [monitoring.cluster_alerts.email_notifications.email_address] will be required for email notifications to work in 8.0.&quot;
  log   [22:30:22.482] [info][plugins-system] Setting up [100] plugins: [taskManager,licensing,globalSearch,globalSearchProviders,banners,code,usageCollection,xpackLegacy,telemetryCollectionManager,telemetry,telemetryCollectionXpack,kibanaUsageCollection,securityOss,share,newsfeed,mapsLegacy,kibanaLegacy,translations,legacyExport,embeddable,uiActionsEnhanced,expressions,charts,esUiShared,bfetch,data,home,observability,console,consoleExtensions,apmOss,searchprofiler,painlessLab,grokdebugger,management,indexPatternManagement,advancedSettings,fileUpload,savedObjects,visualizations,visTypeVislib,visTypeVega,visTypeTimelion,features,licenseManagement,watcher,canvas,visTypeTagcloud,visTypeTable,visTypeMetric,visTypeMarkdown,tileMap,regionMap,visTypeXy,graph,timelion,dashboard,dashboardEnhanced,visualize,visTypeTimeseries,inputControlVis,discover,discoverEnhanced,savedObjectsManagement,spaces,security,savedObjectsTagging,maps,lens,reporting,lists,encryptedSavedObjects,dashboardMode,dataEnhanced,cloud,upgradeAssistant,snapshotRestore,fleet,indexManagement,rollup,remoteClusters,crossClusterReplication,indexLifecycleManagement,enterpriseSearch,beatsManagement,transform,ingestPipelines,eventLog,actions,alerts,triggersActionsUi,stackAlerts,ml,securitySolution,case,infra,monitoring,logstash,apm,uptime]
  log   [22:30:22.483] [info][plugins][taskManager] TaskManager is identified by the Kibana UUID: xxxxxx
  ...
    
</code></pre>
<p>如果是后台启动：</p>
<pre><code class="language-bash">[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7e1b121f0d0a171d0d1b1f0c1d163e2833534e534f4a531d1b100a110d">[email&#160;protected]</a> kibana-7.12.0-linux-x86_64]$ nohup ./bin/kibana &amp;
    
</code></pre>
<ul>
<li><strong>界面访问</strong></li>
</ul>
<p><img src="assets/es-install-1.png" alt="img" /></p>
<p>可以导入simple data</p>
<p><img src="assets/es-install-2.png" alt="img" /></p>
<p>查看数据</p>
<p><img src="assets/es-install-3.png" alt="img" /></p>
<h2>配置密码访问</h2>
<blockquote>
<p>使用基本许可证时，默认情况下禁用Elasticsearch安全功能。由于我测试环境是放在公网上的，所以需要设置下密码访问。相关文档可以参考<a href="https://www.elastic.co/guide/en/elasticsearch/reference/7.12/security-minimal-setup.html">这里  </a></p>
</blockquote>
<ol>
<li>停止kibana和elasticsearch服务</li>
<li>将<code>xpack.security.enabled</code>设置添加到ES_PATH_CONF/elasticsearch.yml文件并将值设置为true</li>
<li>启动elasticsearch (<code>./bin/elasticsearch -d</code>)</li>
<li>执行如下密码设置器，<code>./bin/elasticsearch-setup-passwords interactive</code>来设置各个组件的密码</li>
<li>将elasticsearch.username设置添加到KIB_PATH_CONF/kibana.yml 文件并将值设置给elastic用户： <code>elasticsearch.username: &quot;elastic&quot;</code></li>
<li>创建kibana keystore, <code>./bin/kibana-keystore create</code></li>
<li>在kibana keystore 中添加密码 <code>./bin/kibana-keystore add elasticsearch.password</code></li>
<li>重启kibana 服务即可 <code>nohup ./bin/kibana &amp;</code></li>
</ol>
<p>然后就可以使用密码登录了：</p>
<p><img src="assets/es-install-4.png" alt="img" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;入门：查询和聚合的基础使用.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43400d8e8e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
