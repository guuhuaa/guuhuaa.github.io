<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>24  CICD：容器化后如何实现持续集成与交付？（上）.md</title>
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

                    
                    <a href="00&#32;溯本求源，吃透&#32;Docker！.md">00 溯本求源，吃透 Docker！.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;Docker&#32;安装：入门案例带你了解容器技术原理.md">01  Docker 安装：入门案例带你了解容器技术原理.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;核心概念：镜像、容器、仓库，彻底掌握&#32;Docker&#32;架构核心设计理念.md">02  核心概念：镜像、容器、仓库，彻底掌握 Docker 架构核心设计理念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;镜像使用：Docker&#32;环境下如何配置你的镜像？.md">03  镜像使用：Docker 环境下如何配置你的镜像？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;容器操作：得心应手掌握&#32;Docker&#32;容器基本操作.md">04  容器操作：得心应手掌握 Docker 容器基本操作.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;仓库访问：怎样搭建属于你的私有仓库？.md">05  仓库访问：怎样搭建属于你的私有仓库？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;最佳实践：如何在生产中编写最优&#32;Dockerfile？.md">06  最佳实践：如何在生产中编写最优 Dockerfile？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;Docker&#32;安全：基于内核的弱隔离系统如何保障安全性？.md">07  Docker 安全：基于内核的弱隔离系统如何保障安全性？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;容器监控：容器监控原理及&#32;cAdvisor&#32;的安装与使用.md">08  容器监控：容器监控原理及 cAdvisor 的安装与使用.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;资源隔离：为什么构建容器需要&#32;Namespace&#32;？.md">09  资源隔离：为什么构建容器需要 Namespace ？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;资源限制：如何通过&#32;Cgroups&#32;机制实现资源限制？.md">10  资源限制：如何通过 Cgroups 机制实现资源限制？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;组件组成：剖析&#32;Docker&#32;组件作用及其底层工作原理.md">11  组件组成：剖析 Docker 组件作用及其底层工作原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;网络模型：剖析&#32;Docker&#32;网络实现及&#32;Libnetwork&#32;底层原理.md">12  网络模型：剖析 Docker 网络实现及 Libnetwork 底层原理.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;数据存储：剖析&#32;Docker&#32;卷与持久化数据存储的底层原理.md">13  数据存储：剖析 Docker 卷与持久化数据存储的底层原理.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;文件存储驱动：AUFS&#32;文件系统原理及生产环境的最佳配置.md">14  文件存储驱动：AUFS 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;文件存储驱动：Devicemapper&#32;文件系统原理及生产环境的最佳配置.md">15  文件存储驱动：Devicemapper 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;文件存储驱动：OverlayFS&#32;文件系统原理及生产环境的最佳配置.md">16  文件存储驱动：OverlayFS 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（上）.md">17  原理实践：自己动手使用 Golang 开发 Docker（上）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（下）.md">18  原理实践：自己动手使用 Golang 开发 Docker（下）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">19  如何使用 Docker Compose 解决开发环境的依赖？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">20  如何在生产环境中使用 Docker Swarm 调度容器？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;多阶级构建：Docker&#32;下如何实现镜像多阶级构建？.md">22  多阶级构建：Docker 下如何实现镜像多阶级构建？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;DevOps：容器化后如何通过&#32;DevOps&#32;提高协作效能？.md">23  DevOps：容器化后如何通过 DevOps 提高协作效能？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="24&#32;&#32;CICD：容器化后如何实现持续集成与交付？（上）.md">24  CICD：容器化后如何实现持续集成与交付？（上）.md</a>
                    

                </li>
                <li>

                    
                    <a href="25&#32;&#32;CICD：容器化后如何实现持续集成与交付？（下）.md">25  CICD：容器化后如何实现持续集成与交付？（下）.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;结束语&#32;&#32;展望未来：Docker&#32;的称霸之路.md">26 结束语  展望未来：Docker 的称霸之路.md</a>

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
                        <div><h1>24  CICD：容器化后如何实现持续集成与交付？（上）</h1>
<p>上一讲，我介绍了 DevOps 的概念与 DevOps 的一些思想。DevOps 的思想可以帮助我们缩短上线周期并且提高软件迭代速度，而 CI/CD 则是 DevOps 思想中最重要的部分。</p>
<p>具体来说，CI/CD 是一种通过在应用开发阶段，引入自动化的手段来频繁地构建应用，并且向客户交付应用的方法。它的核心理念是持续开发、持续部署以及持续交付，它还可以让自动化持续交付贯穿于整个应用生命周期，使得开发和运维统一参与协同支持。</p>
<p>下面我们来详细了解下 CI/CD 。</p>
<h3>什么是 CI/CD</h3>
<h4>CI 持续集成（Continuous Integration）</h4>
<p>随着软件功能越来越复杂，一个大型项目要想在规定时间内顺利完成，就需要多位开发人员协同开发。但是，如果我们每个人都负责开发自己的代码，然后集中在某一天将代码合并在一起（称为“合并日”）。你会发现，代码可能会有很多冲突和编译问题，而这个处理过程十分烦琐、耗时，并且需要每一位工程师确认代码是否被覆盖，代码是否完整。这种情况显然不是我们想要看到的，这时持续集成（CI）就可以很好地帮助我们解决这个问题。</p>
<p>CI 持续集成要求开发人员频繁地（甚至是每天）将代码提交到共享分支中。一旦开发人员的代码被合并，将会自动触发构建流程来构建应用，并通过触发自动化测试（单元测试或者集成测试）来验证这些代码的提交，确保这些更改没有对应用造成影响。如果发现提交的代码在测试过程中或者构建过程中有问题，则会马上通知研发人员确认，修改代码并重新提交。通过将以往的定期合并代码的方式，改变为频繁提交代码并且自动构建和测试的方式，可以帮助我们<strong>及早地发现问题和解决冲突，减少代码出错。</strong></p>
<p>传统 CI 流程的实现十分复杂，无法做到标准化交付，而当我们的应用容器化后，应用构建的结果就是 Docker 镜像。代码检查完毕没有缺陷后合并入主分支。此时启动构建流程，构建系统会自动将我们的应用打包成 Docker 镜像，并且推送到镜像仓库。</p>
<h4>CD 持续交付（Continuous Delivery）</h4>
<p>当我们每次完成代码的测试和构建后，我们需要将编译后的镜像快速发布到测试环境，这时我们的持续交付就登场了。持续交付要求我们实现自动化准备测试环境、自动化测试应用、自动化监控代码质量，并且自动化交付生产环境镜像。</p>
<p>在以前，测试环境的构建是非常耗时的，并且很难保证测试环境和研发环境的一致性。但现在，借助于容器技术，我们可以很方便地构建出一个测试环境，并且可以保证开发和测试环境的一致性，这样不仅可以提高测试效率，还可以提高敏捷性。</p>
<p>容器化后的应用交付过程是这样的，我们将测试的环境交由 QA 来维护，当我们确定好本次上线要发布的功能列表时，我们将不同开发人员开发的 feature 分支的代码合并到 release 分支。然后由 QA 来将构建镜像部署到测试环境，结合自动测试和人工测试、自动检测和人工记录，形成完整的测试报告，并且把测试过程中遇到的问题交由开发人员修改，开发修改无误后再次构建测试环境进行测试。测试没有问题后，自动交付生产环境的镜像到镜像仓库。</p>
<h4>CD 持续部署（Continuous Deployment）</h4>
<p>CD 不仅有持续交付的含义，还代表持续部署。经测试无误打包完生产环境的镜像后，我们需要把镜像部署到生产环境，持续部署是最后阶段，它作为持续交付的延伸，可以自动将生产环境的镜像发布到生产环境中。</p>
<p>部署业务首先需要我们有一个资源池，实现资源自动化供给，而且有的应用还希望有自动伸缩的能力，根据外部流量自动调整容器的副本数，而这一切在容器云中都将变得十分简单。</p>
<p>我们可以想象，如果有客户提出了反馈，我们通过持续部署在几分钟内，就能在更改完代码的情况下，将新的应用版本发布到生产环境中（假设通过了自动化测试），这时我们就可以实现快速迭代，持续接收和整合用户的反馈，将用户体验做到极致。</p>
<p>讲了这么多概念，也许你会感觉比较枯燥乏味。下面我们就动动手，利用一些工具搭建一个 DevOps 环境。</p>
<p>搭建 DevOps 环境的工具非常多，这里我选择的工具为 Jenkins、Docker 和 GitLab。Jenkins 和 Docker 都已经介绍过了，这里我再介绍一下 Gitlab。</p>
<p>Gitlab 是由 Gitlab Inc. 开发的一款基于 Git 的代码托管平台，它的功能和 GitHub 类似，可以帮助我们存储代码。除此之外，GitLab 还具有在线编辑 wiki、issue 跟踪等功能，另外最新版本的 GitLab 还集成了 CI/CD 功能，不过这里我们仅仅使用 GitLab 的代码存储功能， CI/CD 还是交给我们的老牌持续集成工具 Jenkins 来做。</p>
<h3>Docker+Jenkins+GitLab 搭建 CI/CD 系统</h3>
<p>软件安装环境如下。</p>
<ul>
<li>操作系统：CentOS 7</li>
<li>Jenkins：tls 长期维护版</li>
<li>Docker：18.06</li>
<li>GitLab：13.3.8-ce.0</li>
</ul>
<h4>第一步：安装 Docker</h4>
<p>安装 Docker 的步骤可以在[第一讲]的内容中找到，这里就不再赘述。Docker 环境准备好后，我们就可以利用 Docker 来部署 GitLab 和 Jenkins 了。</p>
<h4>第二步：安装 GitLab</h4>
<p>GitLab 官方提供了 GitLab 的 Docker 镜像，因此我们只需要执行以下命令就可以快速启动一个 GitLab 服务了。</p>
<pre><code>$ docker run -d \

--hostname localhost \

-p 8080:80 -p 2222:22 \

--name gitlab \

--restart always \

--volume /tmp/gitlab/config:/etc/gitlab \

--volume /tmp/gitlab/logs:/var/log/gitlab \

--volume /tmp/gitlab/data:/var/opt/gitlab \

gitlab/gitlab-ce:13.3.8-ce.0
</code></pre>
<p>这个启动过程可能需要几分钟的时间。当服务启动后我们就可以通过 <a href="http://localhost:8080/">http://localhost:8080</a> 访问到我们的 GitLab 服务了。</p>
<p><img src="assets/CgqCHl-05ceAOEtOAAC7xTjpRgo536.png" alt="Drawing 0.png" /></p>
<p>图1 GitLab 设置密码界面</p>
<p>第一次登陆，GitLab 会要求我们设置管理员密码，我们输入管理员密码后点击确认即可，之后 GitLab 会自动跳转到登录页面。</p>
<p><img src="assets/CgqCHl-05eKAftEiAACO_hts6R8497.png" alt="Drawing 1.png" /></p>
<p>图2 GitLab 登录界面</p>
<p>然后输入默认管理员用户名：<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="5332373e3a3d13362b323e233f367d303c3e">[email&#160;protected]</a>，密码为我们上一步设置的密码。点击登录即可登录到系统中，至此，GitLab 已经安装成功。</p>
<h4>第三步：安装 Jenkins</h4>
<p>Jenkins 官方提供了 Jenkins 的 Docker 镜像，我们使用 Jenkins 镜像就可以一键启动一个 Jenkins 服务。命令如下：</p>
<pre><code># docker run -d --name=jenkins \

-p 8888:8080 \

-u root \

--restart always \

-v /var/run/docker.sock:/var/run/docker.sock \

-v /usr/bin/docker:/usr/bin/docker \

-v /tmp/jenkins_home:/var/jenkins_home \

jenkins/jenkins:lts
</code></pre>
<blockquote>
<p>这里，我将 docker.sock 和 docker 二进制挂载到了 Jenkins 容器中，是为了让 Jenkins 可以直接调用 docker 命令来构建应用镜像。</p>
</blockquote>
<p>Jenkins 的默认密码会在容器启动后打印在容器的日志中，我们可以通过以下命令找到 Jenkins 的默认密码，星号之间的类似于一串 UUID 的随机串就是我们的密码。</p>
<pre><code>$ docker logs -f jenkins

unning from: /usr/share/jenkins/jenkins.war

webroot: EnvVars.masterEnvVars.get(&quot;JENKINS_HOME&quot;)

2020-10-31 16:13:06.472+0000 [id=1]	INFO	org.eclipse.jetty.util.log.Log#initialized: Logging initialized @292ms to org.eclipse.jetty.util.log.JavaUtilLog

2020-10-31 16:13:06.581+0000 [id=1]	INFO	winstone.Logger#logInternal: Beginning extraction from war file

2020-10-31 16:13:08.369+0000 [id=1]	WARNING	o.e.j.s.handler.ContextHandler#setContextPath: Empty contextPath

... 省略部分启动日志

Jenkins initial setup is required. An admin user has been created and a password generated.

Please use the following password to proceed to installation:

*************************************************************

*************************************************************

*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.

Please use the following password to proceed to installation:

fb3499944e4845bba9d4b7d9eb4e3932

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************

*************************************************************

*************************************************************

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

2020-10-31 16:17:07.577+0000 [id=28]	INFO	jenkins.InitReactorRunner$1#onAttained: Completed initialization

2020-10-31 16:17:07.589+0000 [id=21]	INFO	hudson.WebAppMain$3#run: Jenkins is fully up and running
</code></pre>
<p>之后，我们通过访问 <a href="http://localhost:8888/">http://localhost:8888</a> 就可以访问到 Jenkins 服务了。</p>
<p><img src="assets/Ciqc1F-05giAJYDhAADCpDZzl2M065.png" alt="Drawing 2.png" /></p>
<p>图3 Jenkins 登录界面</p>
<p>然后将日志中的密码粘贴到密码框即可，之后 Jenkins 会自动初始化，我们根据引导，安装推荐的插件即可。</p>
<p><img src="assets/Ciqc1F-05hSAHd7VAAEpFeu4qfY218.png" alt="Drawing 3.png" /></p>
<p>图4 Jenkins 引导页面</p>
<p>选择好安装推荐的插件后，Jenkins 会自动开始初始化一些常用插件。界面如下：</p>
<p><img src="assets/Ciqc1F-05h-AUSiFAAEAxHFCt30058.png" alt="Drawing 4.png" /></p>
<p>图5 Jenkins 插件初始化</p>
<p>插件初始化完后，创建管理员账户和密码，输入用户名、密码和邮箱等信息，然后点击保存并完成即可。</p>
<p><img src="assets/Ciqc1F-05iaANJXNAABXftlfsvQ115.png" alt="Drawing 5.png" /></p>
<p>图6 Jenkins 创建管理员</p>
<p>这里，确认 Jenkins 地址，我们就可以进入到 Jenkins 主页了。</p>
<p><img src="assets/Ciqc1F-05i2AR2lRAADHULl7Ysk145.png" alt="Drawing 6.png" /></p>
<p>图7 Jenkins 主页</p>
<p>然后在系统管理 -&gt; 插件管理 -&gt; 可选插件处，搜索 GitLab 和 Docker ，分别安装相关插件即可，以便我们的 Jenkins 服务和 GitLab 以及 Docker 可以更好地交互。</p>
<p><img src="assets/Ciqc1F-05j2AfmTUAAGVJGSmG1g804.png" alt="Drawing 7.png" />
<img src="assets/Ciqc1F-05kKAMr27AAGh4SQTNsU299.png" alt="Drawing 8.png" /></p>
<p>图8 Jenkins 插件安装</p>
<p>等待插件安装完成， 重启 Jenkins ，我们的 Jenkins 环境就准备完成了。</p>
<p>现在，我们的 Docker+Jenkins+GitLab 环境已经准备完成，后面只需要把我们的代码推送到 GitLab 中，并做相关的配置即可实现推送代码自动构建镜像和发布。</p>
<h3>结语</h3>
<p>Docker 的出现解决了 CI/CD 流程中的各种问题，Docker 交付的镜像不仅包含应用程序，也包含了应用程序的运行环境，这很好地解决了开发和线上环境不一致问题。同时 Docker 的出现也极大地提升了 CI/CD 的构建效率，我们仅仅需要编写一个 Dockerfile 并将 Dockerfile 提交到我们的代码仓库即可快速构建出我们的应用，最后，当我们构建好 Docker 镜像后 Docker 可以帮助我们快速发布及更新应用。</p>
<p>那么，你知道 Docker 还可以帮助我们解决 CI/CD 流程中的哪些问题吗？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="23&#32;&#32;DevOps：容器化后如何通过&#32;DevOps&#32;提高协作效能？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="25&#32;&#32;CICD：容器化后如何实现持续集成与交付？（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a41ef14645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E7%94%B1%E6%B5%85%E5%85%A5%E6%B7%B1%E5%90%83%E9%80%8F%20Docker-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
