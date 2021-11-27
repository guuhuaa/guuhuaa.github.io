<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>06  Nginx 在系统架构中的作用.md</title>
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

                    <a class="current-tab" href="06&#32;&#32;Nginx&#32;在系统架构中的作用.md">06  Nginx 在系统架构中的作用.md</a>
                    

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

                    
                    <a href="17&#32;&#32;如何应对&#32;Redis&#32;缓存穿透、击穿和雪崩？.md">17  如何应对 Redis 缓存穿透、击穿和雪崩？.md</a>

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
                        <div><h1>06  Nginx 在系统架构中的作用</h1>
<p>通过上一模块的学习，相信你已经掌握了 JMeter 工具的核心用法和技能，并且可以在 JMeter工具使用方面游刃有余。这些内容不仅仅可以帮助你提升工作效率，而且能够通过二次开发解决团队内部的定制化需求。</p>
<p>这一讲我将带你认识一个常用的高性能中间件 Nginx，在正式学习该讲之前，我先跟你聊聊为什么要学习 Nginx，有一位细心的读者给我留言：</p>
<blockquote>
<p>第二模块好像都是在围绕如何写一份优秀的性能方案展开，为什么有一篇关于 Nginx 的文章呢？</p>
</blockquote>
<p>首先不得不说这个同学的行为很值得我们学习，通过大纲尝试去理清学习的整体架构和逻辑。</p>
<p>很多同学向我反馈在写方案时有一个核心痛点，即不知道如何制定性能测试的目标。都说要参考真实数据，公司也没有提供相关的查询接口，所以不清楚去哪里获取用户的访问数据。而 <strong>Nginx 作为业内最常用的代理服务器</strong>，较为详细地记录了用户的访问数据，而且在分布式部署性能优化方面也发挥了积极的作用，所以说到性能测试，Nginx 是不得不提的一个中间件。</p>
<p>本讲就带你学习 Nginx 在应用架构中的作用，并从性能测试角度看如何利用 Nginx 数据统计用户访问量。</p>
<h3>Nginx 重要的两个概念</h3>
<h4>代理</h4>
<p>首先要来解释一下什么是代理，正向代理和反向代理是什么意思？各自作用是什么？不少同学经常听到这些名词，但往往分不清楚具体区别是什么。</p>
<p><strong>什么是代理？</strong></p>
<p>举个例子，比如你很想到某公司去做测试，对方公司的测试主管并不认识你，你也不知道这位测试主管的联系方式，但是你的朋友小王认识，他帮你推荐了简历，此时的小王就起到代理的作用，相当于一个渠道。</p>
<p><strong>正向代理</strong></p>
<p>正向代理的特点是你非常清楚地知道你要去哪儿，访问什么服务器，但服务器并不关心你的出发地是哪里，它只知道你从哪个代理服务器过来。</p>
<p>举个例子，北京去哈尔滨的高铁班次，对于目的地哈尔滨而言，它只知道这部分人是从北京过来的，但是并不清楚这些人之前是不是先从上海或者其他地方先到北京，再转车过来。</p>
<p><strong>反向代理</strong></p>
<p>刚刚说了正向代理，那反向代理又是什么呢？我先来说一下应用场景，比如我们的内部服务器集群，是不可能直接暴露出来让外网访问的，这样安全风险就非常大；再比如现在很多网站为了提高性能都采用了分布式部署，通过多台服务器来缓减服务端的压力，这些都可以通过 Nginx 来完成。</p>
<p>那我们的外网用户如何能够访问到内部的应用呢，Nginx 可以暴露端口给外网用户访问，当接收到请求之后分发给内部的服务器，此时的 Nginx 扮演的是<strong>反向代理的角色</strong>。这样一个过程，客户端是明确的，但对于访问到哪台具体的应用服务器是不明确的。就好像一个上海飞北京的班次，可能还有很多乘客到达北京之后会去沈阳、哈尔滨等，对于出发地上海而言，这个是不关心的。</p>
<h4>负载均衡</h4>
<p>负载均衡是 Nginx 最重要也是最常见的功能，为什么需要负载均衡呢？你可以想一想，比如你线上只有一台应用服务器，如下图所示。</p>
<p><img src="assets/Ciqc1GAOtASAFkMnAAB8g0S7vEo985.png" alt="-1.png" /></p>
<p>但是随着用户体量的上升，一台服务器并不能支撑现有用户的访问，那你就会考虑使用两台或者多台服务器，如下图所示：</p>
<p><img src="assets/CgqCHmAOtBuAdrykAADniCVZ-pg926.png" alt="-2.png" /></p>
<p>那用户如何能够相对均匀地访问到这些服务器呢，这就需要你去了解 Nginx 的负载均衡策略，简单来说，就是 Nginx 如何分发这些请求到后面的应用服务器集群，下面我介绍下 Nginx 的三种分配策略。</p>
<p><strong>（1）轮询</strong></p>
<p>也就是使用平均分配的方式，将每个请求依次分配到配置的后端服务器上。除非有服务宕机，才会停止分发。如下代码所示：</p>
<pre><code>upstream localhost {

//分发到各应用服务

      server  127.0.0.1:7070;

      server  127.0.0.1:7071;

    }

    server{

//Nginx核心监听端口

        listen 8012;

        server_name localhost;

        location / {

                proxy_pass         http://localhost;

                proxy_set_header   Host             $host;

                proxy_set_header   X-Real-IP        $remote_addr;

                proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;

        }

}
</code></pre>
<p><strong>（2）权重</strong></p>
<p>权重即配置轮询的比重，为什么需要这么配置呢？在真实的互联网场景下，很多服务器上都会配置多个应用，这样会导致每台服务器的资源占用不一致，所以在分布式部署配置下也需要注意这一点：</p>
<ul>
<li>相对空闲的机器可以多配置访问比例；</li>
<li>比较繁忙的机器可以少配置一些。</li>
</ul>
<p>如下代码所示，其中 ip1、ip2 以及 port 需要配置你实际的部署 ip 和 port。</p>
<pre><code>     upstream test {

         server ip1:8080 weight=9;

         server ip2:8081 weight=1;

}
</code></pre>
<p><strong>（3）ip_hash</strong></p>
<p>但上面两种配置方式在电商场景下有个很常见的问题，比如你登录了一个网站，登录信息已经保存到 a 机器，但当你做后续操作时的请求会到 b 机器，那么就获取不到你原来登录的信息，此时你就需要重新登录了。这样的情况是用户肯定不能接受的，ip_hash 模式就可以很好地解决这个问题，让每次访问能基于同一用户访问固定的服务器。</p>
<p>ip_hash 模式配置示例如下：</p>
<pre><code>    upstream test {

    ip_hash;

    server localhost:8080;

    server localhost:8081;

}
</code></pre>
<p>接着我们来看下如何基于 Nginx 记录的数据去分析用户访问请求分布，在讲下文之前，按照我的习惯，我想先说一说为什么我要通过 shell 命令去分析 Nginx 日志。</p>
<p>首先对于测试同学而言，比较熟练地掌握了 Python 或者 Java 的用法，但对于 Linux 中的 shell 命令不是很熟悉，也有同学说 shell 能做的我觉得 Python 也可以实现。我想对于性能测试而言，处理效率是一个我们都比较关心的问题。在 Linux 服务器上，你可以处理数据的级别达到百万条以上，对于 Linux 上的文本操作而言，相对于 Python 或者 Java，shell 在处理效率方面有着得天独厚的优势，所以掌握基础的 shell 命令还是必要的。</p>
<p>再说我为什么会选择 Nginx 日志去分析，这也得从互联网行业的现状说起：</p>
<ul>
<li>对于大型互联网公司，关于获取分析日志我想早已有平台化支持，一键就可以导出你需要的用户数据访问报表；</li>
<li>而对于中小公司的测试来说，去哪里获取可能都不是很清楚。</li>
</ul>
<p>所以我选择了使用 Nginx 这种比较原生的方式去讲解，这样对于使用过平台化操作的同学也可以了解一些底层的逻辑操作，也让没有接触过这方面数据统计的同学掌握其中一种实现方法。</p>
<h3>Linux 的 shell 命令</h3>
<p>Linux 的 shell 命令常见的文本操作命令有 awk、sed、sort、wc 等，通过这些命令的熟练掌握和搭配使用，相信你可以对 Linux 服务器上的文本处理如鱼得水。</p>
<h4>awk</h4>
<p>awk 可以将文本中的内容<strong>按行去读取</strong>，然后将读取出来的行按照规定的分隔符去提取你所需要的内容。</p>
<p>awk 常用参数是 -F 指定分隔符。</p>
<p>比如以下代码就是以 : 为分隔符，寻找以 root 开头的行数据，打印第 7 列。</p>
<pre><code># awk -F : '/^root/{print $7}' /etc/passwd

/bin/bash
</code></pre>
<p>以下代码表示以 begin 开头、end 结尾，打印第 1 列数据。</p>
<pre><code>代码块示例

# awk -F : 'BEGIN{print &quot;begin&quot;}{print $1} END{print &quot;end&quot;}' /etc/passwd

begin

root

..

end
</code></pre>
<h4>Sed</h4>
<p>Sed 是一个<strong>流编辑器</strong>，一次只能处理一行内容，需要注意的是 sed 并不改变文本本身的内容，它只是把结果存放在<strong>临时缓冲区</strong>中。</p>
<p>sed 常用的参数有：</p>
<ul>
<li>a 表示新增；</li>
<li>i 表示插入；</li>
<li>c 表示取代；</li>
<li>d 表示删除。</li>
</ul>
<p>举个例子，我们设置一个文本文件，每行只有一个数字，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b4c6dbdbc0f4fef0">[email&#160;protected]</a> data]# cat sed.txt 

1

2

3
</code></pre>
<p>在第一行下新增 4：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="abd9c4c4dfebe1ef">[email&#160;protected]</a> data]# sed '1a 4' sed.txt 

1

4

2

3
</code></pre>
<p>看下原来的文本，你会发现没有任何改动，如下代码所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ccbea3a3b88c8688">[email&#160;protected]</a> data]# cat sed.txt 

1

2

3
</code></pre>
<h4>Sort</h4>
<p>Sort 的默认方式就是把第一列根据 ASCII 值排序输出。常用参数有：</p>
<ul>
<li>-n，依照数值的大小排序；</li>
<li>-r，以相反的顺序来排序；</li>
<li>-k，选择以某个区间进行排序。</li>
</ul>
<p>举个简单的示例，将上述的 sed.txt 倒序输出，如下代码所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3b4954544f7b717f">[email&#160;protected]</a> data]# sort -r sed.txt 

3

2

1
</code></pre>
<h4>uniq</h4>
<p>uniq 用于检查或者统计文本出现的重复行，常用参数是 -c，它用于<strong>连续重复行次数的统计</strong>。</p>
<p>我们构造一个 uniq.txt，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="aedcc1c1daeee4ea">[email&#160;protected]</a> data]# cat uniq.txt 

hello

hello

cctester

cctester

cctester

com
</code></pre>
<p>然后对 uniq.txt 进行重复数据统计，并根据重复次数由大到小排序，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="21534e4e55616b65">[email&#160;protected]</a> data]# uniq -c uniq.txt |sort -r

      3 cctester

      2 hello

      1 com
</code></pre>
<p>学完了这些基础命令，我带你来看 Nginx 日志分析，如果你不清楚你的 Nginx 日志地址，查看nginx.conf 文件的配置即可，指定日志路径如下所示：</p>
<pre><code>    access_log  /data/logs/access.log  main;
</code></pre>
<p>其中部分的日志显示，如下所示：</p>
<pre><code>120.204.101.238 - - [29/Nov/2020:14:19:39 +0800] &quot;GET /hello/map HTTP/1.1&quot; 200 202 

47.92.11.105 - - [29/Nov/2020:14:19:39 +0800] &quot;GET /hello/map HTTP/1.1&quot; 200 202 

185.39.101.238 - - [29/Nov/2020:14:19:39 +0800] &quot;GET /hello/list HTTP/1.1&quot; 200 150 &quot;-

101.132.114.23 - - [29/Nov/2020:14:19:39 +0800] &quot;GET /hello/list HTTP/1.1&quot; 200 150 &quot;-

120.204.101.238 - - [29/Nov/2020:14:19:39 +0800] &quot;POST /v1/login HTTP/1.1&quot; 200 36 &quot;-
</code></pre>
<p>观察上述的日志，是以空格为分隔符号，第一行第一列是 120.204.101.238，第一行第二列是 -，以此类推，打印第 7 列，如下所示：</p>
<pre><code> awk '{print $7}'  access.log 

/hello/list

/v1/login

/hello/list

/hello/map
</code></pre>
<p>你也可以自行验证下输出是否符合预期。</p>
<p>接着我基于这份日志统计访问接口的比例分布，使用如下命令：</p>
<pre><code>cat access.log |awk '{print $7}'|sort|uniq -c|sort -n -k -r
</code></pre>
<p>这个命令，是提取 acccess.log 的第 7 列，也就是接口路径：</p>
<ul>
<li>先 sort 排序，这样可以将相同的接口访问路径合并一起；</li>
<li>再使用 uniq -c 统计连续访问的次数；</li>
<li>最后根据访问次数排序，便可以得到如下结果。</li>
</ul>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="cebca1a1ba8e848a">[email&#160;protected]</a> logs]# cat access.log |awk '{print $7}'|sort|uniq -c|sort -n -k 1 -r

  87280 /hello/list

  18892 /hello/map

  12846 /v1/login
</code></pre>
<p>通过输出结果可以看出第一列就是给定日志内的接口访问次数统计，比如 87280 就是 /hello/list 的访问次数。</p>
<h3>总结</h3>
<p>通过本讲的学习，你已经相对全面地了解了 Nginx 在系统架构中的作用，通过对访问日志的分析，你也能够获取用户的基本访问情况。在实际工作过程中，面对没有原始访问数据的情况下，你就多了一条思路、一种解决方案。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="07&#32;&#32;你真的知道如何制定性能测试的目标吗？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435b7ae874645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
