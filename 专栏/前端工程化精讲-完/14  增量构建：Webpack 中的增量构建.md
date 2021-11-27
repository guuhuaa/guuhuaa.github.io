<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14  增量构建：Webpack 中的增量构建.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;建立上帝视角，全面系统掌握前端效率工程化.md">00 开篇词  建立上帝视角，全面系统掌握前端效率工程化.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;项目基石：前端脚手架工具探秘.md">01  项目基石：前端脚手架工具探秘.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;界面调试：热更新技术如何开着飞机修引擎？.md">02  界面调试：热更新技术如何开着飞机修引擎？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;构建提速：如何正确使用&#32;SourceMap？.md">03  构建提速：如何正确使用 SourceMap？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;接口调试：Mock&#32;工具如何快速进行接口调试？.md">04  接口调试：Mock 工具如何快速进行接口调试？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;编码效率：如何提高编写代码的效率？.md">05  编码效率：如何提高编写代码的效率？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;团队工具：如何利用云开发提升团队开发效率？.md">06  团队工具：如何利用云开发提升团队开发效率？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;低代码工具：如何用更少的代码实现更灵活的需求.md">07  低代码工具：如何用更少的代码实现更灵活的需求.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;无代码工具：如何做到不写代码就能高效交付？.md">08  无代码工具：如何做到不写代码就能高效交付？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;构建总览：前端构建工具的演进.md">09  构建总览：前端构建工具的演进.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;流程分解：Webpack&#32;的完整构建流程.md">10  流程分解：Webpack 的完整构建流程.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;编译提效：如何为&#32;Webpack&#32;编译阶段提速？.md">11  编译提效：如何为 Webpack 编译阶段提速？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;打包提效：如何为&#32;Webpack&#32;打包阶段提速？.md">12  打包提效：如何为 Webpack 打包阶段提速？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;缓存优化：那些基于缓存的优化方案.md">13  缓存优化：那些基于缓存的优化方案.md</a>

                </li>
                <li>

                    <a class="current-tab" href="14&#32;&#32;增量构建：Webpack&#32;中的增量构建.md">14  增量构建：Webpack 中的增量构建.md</a>
                    

                </li>
                <li>

                    
                    <a href="15&#32;&#32;版本特性：Webpack&#32;5&#32;中的优化细节.md">15  版本特性：Webpack 5 中的优化细节.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;无包构建：盘点那些&#32;No-bundle&#32;的构建方案.md">16  无包构建：盘点那些 No-bundle 的构建方案.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;部署初探：为什么一般不在开发环境下部署代码？.md">17  部署初探：为什么一般不在开发环境下部署代码？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;工具盘点：掌握那些流行的代码部署工具.md">18  工具盘点：掌握那些流行的代码部署工具.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;安装提效：部署流程中的依赖安装效率优化.md">19  安装提效：部署流程中的依赖安装效率优化.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;流程优化：部署流程中的构建流程策略优化.md">20  流程优化：部署流程中的构建流程策略优化.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;容器方案：从构建到部署，容器化方案的优势有哪些？.md">21  容器方案：从构建到部署，容器化方案的优势有哪些？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;案例分析：搭建基本的前端高效部署系统.md">22  案例分析：搭建基本的前端高效部署系统.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语&#32;&#32;前端效率工程化的未来展望.md">23 结束语  前端效率工程化的未来展望.md</a>

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
                        <div><h1>14  增量构建：Webpack 中的增量构建</h1>
<p>开始课程前，我先来解答上一节课的思考题：课程中介绍的几种支持缓存的插件（TerserWebpackPlugin，CSSMinimizerWebpackPlugin）和 Loader（babel-loader，cache-loader）在缓存方面有哪些相同的配置项呢？</p>
<p>通过对比不难发现，这些工具通常至少包含两个配置项：第一项用于指定是否开启缓存，以及指定缓存目录（值为 true 时使用默认目录，指定目录时也表示开启），配置名称通常是 cache 或 cacheDirectory；第二项用于指定缓存标识符的计算参数，通常默认值是一个包含多维度参数的对象，例如这个工具模块的版本号、配置项对象、文件路径和内容等。这个配置项是为了确保缓存使用的安全性，防止当源代码不变但相关构建参数发生变化时对旧缓存的误用。</p>
<p>下面开始本节课的学习。曾经有同事问我一个问题：为什么我只改了一行代码，却需要花 5 分钟才能构建完成？</p>
<p>你可能也有同样的疑问，但经过前面几节关于 Webpack 构建原理和优化的课程后，相信已经可以解答。尽管只改动了一行代码，但是在执行构建时，要完整执行所有模块的编译、优化和生成产物的处理过程，而不是只需要处理所改动的文件。大多数情况下，我们能做的是像前面几节课中讨论的那样，通过各种优化方案提升整体构建的效率。</p>
<p>但是只编译打包所改动的文件真的不能实现吗？这节课我们就来讨论这个话题（课程里完整的示例代码参见 <a href="https://github.com/fe-efficiency/lessons_fe_efficiency/tree/master/14_incremental_build">14_incremental_build</a>）。</p>
<h3>Webpack 中的增量构建</h3>
<p>上述只构建改动文件的处理过程在 Webpack 中是实际存在的，你可能也很熟悉，那就是在<strong>开启 devServer</strong>的时候，当我们执行 webpack-dev-server 命令后，Webpack 会进行一次初始化的构建，构建完成后启动服务并进入到等待更新的状态。当本地文件有变更时，Webpack 几乎瞬间将变更的文件进行编译，并将编译后的代码内容推送到浏览器端。你会发现，这个文件变更后的处理过程就符合上面所说的只编译打包改动的文件的操作，这就称为“<strong>增量构建”</strong>。我们通过示例代码进行验证（<em>npm run dev</em>），如下面的图片：</p>
<p><img src="assets/CgqCHl9sTsWAbetxAAGoldlDrIw704.png" alt="Drawing 0.png" />
<img src="assets/Ciqc1F9sTsmAJc8YAADz9x_Zsvo780.png" alt="Drawing 1.png" /></p>
<p>可以看到，在开发服务模式下，初次构建编译了 47 个模块，完整的构建时间为 3306ms。当我们改动其中一个源码文件后，日志显示 Webpack 只再次构建了这一个模块，因此再次构建的时间非常短（24ms）。那么为什么在开发服务模式下可以实现增量构建的效果，而在生产环境下不行呢？下面我们来分析影响结果的因素。</p>
<h3>增量构建的影响因素</h3>
<h4>watch 配置</h4>
<p>在上面的增量构建过程中，第一个想到的就是<strong>需要监控文件的变化</strong>。显然，只有得知变更的是哪个文件后，才能进行后续的针对性处理。要实现这一点也很简单，在“第 2 课时|界面调试：热更新技术如何开着飞机修引擎？”中已经介绍过，在 Webpack 中<strong>启用 watch 配置</strong>即可，此外在使用 devServer 的情况下，该选项会<strong>默认开启</strong>。那么，如果在生产模式下开启 watch 配置，是不是再次构建时，就会按增量的方式执行呢？我们仍然通过示例验证（<em>npm run build:watch</em>），如下面的图片所示：</p>
<p><img src="assets/CgqCHl9sTtOAPzPRAAHMQJnGHlo474.png" alt="Drawing 2.png" />
<img src="assets/CgqCHl9sTtiAB2seAAG0v0B0ORQ594.png" alt="Drawing 3.png" /></p>
<p>从结果中可以发现，在生产模式下开启 watch 配置后，相比初次构建，再次构建所编译的模块数量并未减少，即使只改动了一个文件，也仍然会对所有模块进行编译。因此可以得出结论，在生产环境下只开启 watch 配置后的再次构建<strong>并不能</strong>实现增量构建。</p>
<h4>cache 配置</h4>
<p>仔细查阅 Webpack 的配置项文档，会在菜单最下方的“其他选项”一栏中找到 <a href="https://v4.webpack.js.org/configuration/other-options/#cache">cache</a> 选项（需要注意的是我们查阅的是 <strong>Webpack 4 版本的文档</strong>，Webpack 5 中这一选项会有大的改变，会在下一节课中展开讨论）。这一选项的值有两种类型：布尔值和对象类型。一般情况下默认为<strong>false</strong>，即不使用缓存，但在开发模式开启 watch 配置的情况下，cache 的默认值变更为<strong>true</strong>。此外，如果 cache 传值为对象类型，则表示使用该对象来作为缓存对象，这往往用于多个编译器 compiler 的调用情况。</p>
<p>下面我们就来看一下，在生产模式下，如果watch 和 cache 都为 true，结果会如何（npm run build:watch-cache）？如下面的图片所示：</p>
<p><img src="assets/CgqCHl9sTuuAc0_4AAHBe2Lt3do732.png" alt="Drawing 4.png" />
<img src="assets/Ciqc1F9sTvCAY2NvAAEtJYxCA_8121.png" alt="Drawing 5.png" /></p>
<p>正如我们所期望的，再次构建时，在编译模块阶段只对有变化的文件进行了重新编译，实现了<strong>增量编译</strong>的效果。</p>
<p>但是美中不足的是，在优化阶段压缩代码时仍然耗费了较多的时间。这一点很容易理解：</p>
<p>体积最大的 react、react-dom 等模块和入口模块打入了同一个 Chunk 中，即使修改的模块是单独分离的 bar.js，但它的产物名称的变化仍然需要反映在入口 Chunk 的 runtime 模块中。因此入口 Chunk 也需要跟着重新压缩而无法复用压缩缓存数据。根据前面几节课的知识点，我们对配置再做一些优化，将 vendor 分离后再来看看效果，如下面的图片所示：</p>
<p><img src="assets/CgqCHl9sTvqAP1oIAAG2kbb-DGY688.png" alt="Drawing 6.png" />
<img src="assets/CgqCHl9sTv6AYxTKAAFAsmUEZMg953.png" alt="Drawing 7.png" /></p>
<p>可以看到，通过上面这一系列的配置后（<strong>watch + cache</strong>），在生产模式下，最终呈现出了我们期望的<strong>增量构建</strong>效果：有文件发生变化时会自动编译变更的模块，并只对该模块影响到的少量 Chunk 进行优化并更新产物文件版本，而其他产物文件则保持之前的版本。如此，整个构建过程的速度大大提升。</p>
<h3>增量构建的实现原理</h3>
<p>为什么在配置项中需要同时启用 watch 和 cache 配置才能获得增量构建的效果呢？接下来我们从源码层面分析。</p>
<h4>watch 配置的作用</h4>
<p>watch 配置的具体逻辑在 Webpack 的 <a href="https://github.com/webpack/webpack/blob/webpack-4/lib/Watching.js">Watching.js</a> 中。查看源码可以看到，在它构建相关的 _go 方法中，执行的依然是 compiler实例的 compile 方法，这一点与普通构建流程并无区别。真正的区别在于，在 watch 模式下，构建完成后并不自动退出，因此构建上下文的对象（包括前一次构建后的缓存数据对象）都可以保留在内存中，并在 rebuild 时重复使用，如下面的代码所示：</p>
<pre><code>lib/Watching.js

...

_go() {

  ...

  this.compiler.hooks.watchRun.callAsync(this.compiler, err =&gt; {

    const onCompiled = (err, compilation) =&gt; {

      ...

    }

    this.compiler.compile(onCompiled);

  }

}
</code></pre>
<h4>cache 配置的作用</h4>
<p>cache 配置的源码逻辑主要涉及两个文件：<a href="https://github.com/webpack/webpack/blob/webpack-4/lib/CachePlugin.js">CachePlugin.js</a> 和 <a href="https://github.com/webpack/webpack/blob/webpack-4/lib/Compilation.js">Compilation.js</a>。其中 CachePlugin.js 的核心作用是将该插件实例的 cache 属性传入 compilation 实例中，如下面的代码所示：</p>
<pre><code>lib/CachePlugin.js

...

compiler.hooks.thisCompilation.tap(&quot;CachePlugin&quot;, compilation =&gt; {

  compilation.cache = cache;

  ...

}
</code></pre>
<p>而在 Compilation.js 中，运用 cache 的地方有两处：</p>
<ol>
<li>在<strong>编译阶段添加模块时</strong>，若命中缓存<strong>module</strong>，则直接跳过该模块的编译过程（与 cache-loader 等作用于加载器的缓存不同，此处的缓存可直接跳过 Webpack 内置的编译阶段）。</li>
<li>在创建 Chunk 产物代码阶段，若命中缓存<strong>Chunk</strong>，则直接跳过该 Chunk 的产物代码生成过程。</li>
</ol>
<p>如下面的代码所示：</p>
<pre><code>lib/Compilation.js

...

addModule(module, cacheGroup) {

  ...

  if (this.cache &amp;&amp; this.cache[cacheName]) {

    const cacheModule = this.cache[cacheName];

    ...

    //缓存模块存在情况下判断是否需要rebuild

    rebuild = ...

    if (!rebuild) {

      ...

      //无须rebuild情况下返回cacheModule，并标记build:false

      return {

		module: cacheModule,

		issuer: true,

		build: false,

		dependencies: true

	  }      

    }

    ...

  }

  if (this.cache) {

    this.cache[cacheName] = module;

  }

  ...

  //无缓存或需要rebuild情况下返回module，并标记build:true

  return {

	module: module,

	issuer: true,

	build: true,

	dependencies: true

  };

}

...

createChunkAssets() {

  ...

  if ( this.cache &amp;&amp; this.cache[cacheName] &amp;&amp; this.cache[cacheName].hash === usedHash ) {

    source = this.cache[cacheName].source;

  } else {

	source = fileManifest.render();

    ...

  }

}
</code></pre>
<p>以上就是 Webpack 4 中 watch 和 cache 配置的作用原理。通过 Webpack 内置的 cache 插件，将整个构建中相对耗时的两个内部处理环节——编译模块和生成产物，进行缓存的读写处理，从而实现增量构建处理。那么我们是不是就可以在生产环境下直接使用这个方案呢？</p>
<h3>生产环境下使用增量构建的阻碍</h3>
<p>增量构建之所以快是因为将构建所需的数据（项目文件、node_modules 中的文件数据、历史构建后的缓存数据等）都<strong>保留在内存中</strong>。在 watch 模式下保留着构建使用的 Node 进程，使得下一次构建时可以直接读取内存中的数据。</p>
<p>而生产环境下的构建通常在集成部署系统中进行。对于管理多项目的构建系统而言，构建过程是任务式的：任务结束后即结束进程并回收系统资源。对于这样的系统而言，增量构建所需的保留进程与长时间占用内存，通常都是<strong>不可接受的</strong>。</p>
<p>因此，基于内存的缓存数据注定无法运用到生产环境中。要想在生产环境下提升构建速度，<strong>首要条件是将缓存写入到文件系统中</strong>。只有将文件系统中的缓存数据持久化，才能脱离对保持进程的依赖，你只需要在每次构建时将缓存数据读取到内存中进行处理即可。事实上，这也是上一课时中讲到的那些 Loader 与插件中的缓存数据的存储方式。</p>
<p>遗憾的是，Webpack 4 中的 cache 配置<strong>只支持基于内存的缓存</strong>，并不支持文件系统的缓存。因此，我们只能通过上节课讲到的一些支持缓存的第三方处理插件将局部的构建环节应用“<strong>增量处理</strong>”。</p>
<p>不过好消息是 Webpack 5 中<strong>正式支持基于文件系统的持久化缓存</strong>（Persistent Cache）。我们会在下一课时详细讨论包括这一特性在内的 Webpack 5 中的优化点。</p>
<h3>总结</h3>
<p>这节课我们主要讨论了构建处理的一种理想情况：增量构建。增量构建在每次执行构建时，只编译处理内容有修改的少量文件，从而极大地提升构建效率。</p>
<p>在 Webpack 4 中，有两个配置项与增量构建相关：watch 和 cache。当我们启用开发服务器时，这两个选项都是默认启用的，因此可以在开发模式下体验到增量构建带来的速度提升。</p>
<p>从内部原理的角度分析，watch 的作用是保留进程，使得初次构建后的数据对象能够在再次构建时复用。而 cache 的作用则体现在构建过程中，在添加模块与生成产物代码时可以利用 cache 对象进行相应阶段结果数据的读写。显然，这种基于内存的缓存方式无法在生产环境下广泛使用。</p>
<p>今天的<strong>课后思考题</strong>是：在启用增量构建的情况下有时候可能还会遇到 rebuild 很慢的情况，试着分析原因。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;&#32;缓存优化：那些基于缓存的优化方案.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;&#32;版本特性：Webpack&#32;5&#32;中的优化细节.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4352128d0d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%8C%96%E7%B2%BE%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
