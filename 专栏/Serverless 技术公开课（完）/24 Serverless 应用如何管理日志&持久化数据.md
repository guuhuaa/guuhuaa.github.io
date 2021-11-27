<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>24 Serverless 应用如何管理日志&amp;持久化数据.md</title>
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

                    
                    <a href="01&#32;架构的演进.md">01 架构的演进.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;Serverless&#32;的价值.md">02 Serverless 的价值.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;常见&#32;Serverless&#32;架构模式.md">03 常见 Serverless 架构模式.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;Serverless&#32;技术选型.md">04 Serverless 技术选型.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;函数计算简介.md">05 函数计算简介.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;函数计算是如何工作的？.md">06 函数计算是如何工作的？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;函数粘合云服务提供端到端解决方案.md">07 函数粘合云服务提供端到端解决方案.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;函数计算的开发与配置.md">08 函数计算的开发与配置.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;函数的调试与部署.md">09 函数的调试与部署.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;自动化&#32;CI&amp;CD&#32;与灰度发布.md">10 自动化 CI&amp;CD 与灰度发布.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;函数计算的可观测性.md">11 函数计算的可观测性.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;典型案例&#32;1：函数计算在音视频场景实践.md">12 典型案例 1：函数计算在音视频场景实践.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;典型案例&#32;3：十分钟搭建弹性可扩展的&#32;Web&#32;API.md">13 典型案例 3：十分钟搭建弹性可扩展的 Web API.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;Serverless&#32;Kubernetes&#32;容器服务介绍.md">14 Serverless Kubernetes 容器服务介绍.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;Serverless&#32;Kubernetes&#32;应用部署及扩缩容.md">15 Serverless Kubernetes 应用部署及扩缩容.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;使用&#32;Spot&#32;低成本运行&#32;Job&#32;任务.md">16 使用 Spot 低成本运行 Job 任务.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;低成本运行&#32;Spark&#32;数据计算.md">17 低成本运行 Spark 数据计算.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;GPU&#32;机器学习开箱即用.md">18 GPU 机器学习开箱即用.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;基于&#32;Knative&#32;低成本部署在线应用，灵活自动伸缩.md">19 基于 Knative 低成本部署在线应用，灵活自动伸缩.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;快速构建&#32;JenkinsGitlab&#32;持续集成环境.md">20 快速构建 JenkinsGitlab 持续集成环境.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;在线应用的&#32;Serverless&#32;实践.md">21 在线应用的 Serverless 实践.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;通过&#32;IDEMaven&#32;部署&#32;Serverless&#32;应用实践.md">22 通过 IDEMaven 部署 Serverless 应用实践.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;企业级&#32;CICD&#32;工具部署&#32;Serverless&#32;应用的落地实践.md">23 企业级 CICD 工具部署 Serverless 应用的落地实践.md</a>

                </li>
                <li>

                    <a class="current-tab" href="24&#32;Serverless&#32;应用如何管理日志&amp;持久化数据.md">24 Serverless 应用如何管理日志&amp;持久化数据.md</a>
                    

                </li>
                <li>

                    
                    <a href="25&#32;Serverless&#32;应用引擎产品的流量负载均衡和路由策略配置实践.md">25 Serverless 应用引擎产品的流量负载均衡和路由策略配置实践.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;Spring&#32;CloudDubbo&#32;应用无缝迁移到&#32;Serverless&#32;架构.md">26 Spring CloudDubbo 应用无缝迁移到 Serverless 架构.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;SAE&#32;应用分批发布与无损下线的最佳实践.md">27 SAE 应用分批发布与无损下线的最佳实践.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Serverless%20%E6%8A%80%E6%9C%AF%E5%85%AC%E5%BC%80%E8%AF%BE%EF%BC%88%E5%AE%8C%EF%BC%89/28%20%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87%E5%8E%8B%E6%B5%8B%E5%B7%A5%E5%85%B7+%20SAE%20%E5%BC%B9%E6%80%A7%E8%83%BD%E5%8A%9B%E8%BD%BB%E6%9D%BE%E5%BA%94%E5%AF%B9%E5%A4%A7%E4%BF%83.md">28 如何通过压测工具+ SAE 弹性能力轻松应对大促.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;SAE&#32;极致应用部署效率.md">29 SAE 极致应用部署效率.md</a>

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
                        <div><h1>24 Serverless 应用如何管理日志&amp;持久化数据</h1>
<h3>实时日志</h3>
<p><img src="assets/2020-10-26-040934.png" alt="图片1.png" /></p>
<p>首先，SAE 支持查看应用实例分组下各个 Pod 的实时日志。当应用出现异常情况时，可以通过查看 Pod 的实时日志定位问题。当应用运行时，可以在【控制台 - 日志管理菜单下 - 实时日志子菜单】方便地看到应用实例的实时日志。</p>
<h3>文件日志</h3>
<p><img src="assets/2020-10-26-040936.png" alt="图片2.png" /></p>
<p>SAE 将业务文件日志（不包含 stdout 和 stderr 日志）收集并输入 SLS 中，实现无限制行数查看日志、自行聚合分析日志，方便业务日志对接，并按日志使用量计费。</p>
<p>您可以在部署应用时配置日志收集服务，填入需要采集的日志源，对于滚动日志的场景，可以填入通配符进行解决。</p>
<p><img src="assets/2020-10-26-040939.png" alt="图片3.PNG" /></p>
<p>当配置完成后，可以在【控制台 - 日志管理菜单 - 文件日志子菜单】方便地看到采集的文件日志。</p>
<h3>NAS 持久化存储</h3>
<p><img src="assets/2020-10-26-040940.png" alt="图片4.png" /></p>
<p>由于存储在容器中数据是非持久化的，SAE 支持了 NAS 存储功能，解决了应用实例数据持久化和实例间多读共享数据的问题。</p>
<p>您可以通过部署应用来配置持久化存储，选择创建好的 NAS，并填入容器中对应的挂载路径即可。</p>
<p><img src="assets/2020-10-26-040942.png" alt="幻灯片9.PNG" /></p>
<p>当配置完成后，可以通过 cat /proc/mount | grep nfs 命令查看是否挂载成功，或者可以准备 2 个应用实例，A 和 B，分别挂载 NAS。对 A 执行写入命令 echo &quot;hello&quot; &gt; tmp.txt，对 B 执行读取命令 cat tmp.txt。如果 B 中能够读取到在 A 中写入的 hello，表示 NAS 挂载成功。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="23&#32;企业级&#32;CICD&#32;工具部署&#32;Serverless&#32;应用的落地实践.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="25&#32;Serverless&#32;应用引擎产品的流量负载均衡和路由策略配置实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434bd69cf170ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Serverless%20%E6%8A%80%E6%9C%AF%E5%85%AC%E5%BC%80%E8%AF%BE%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
