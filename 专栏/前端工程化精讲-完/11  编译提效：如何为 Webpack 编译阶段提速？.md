<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11  编译提效：如何为 Webpack 编译阶段提速？.md</title>
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

                    <a class="current-tab" href="11&#32;&#32;编译提效：如何为&#32;Webpack&#32;编译阶段提速？.md">11  编译提效：如何为 Webpack 编译阶段提速？.md</a>
                    

                </li>
                <li>

                    
                    <a href="12&#32;&#32;打包提效：如何为&#32;Webpack&#32;打包阶段提速？.md">12  打包提效：如何为 Webpack 打包阶段提速？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;缓存优化：那些基于缓存的优化方案.md">13  缓存优化：那些基于缓存的优化方案.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;增量构建：Webpack&#32;中的增量构建.md">14  增量构建：Webpack 中的增量构建.md</a>

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
                        <div><h1>11  编译提效：如何为 Webpack 编译阶段提速？</h1>
<p>上一课我们聊了 Webpack 的基本工作流程，分析了其中几个主要源码文件的执行过程，并介绍了 Compiler 和 Compilation 两个核心模块中的生命周期 Hooks。</p>
<p>上节课后的思考题是，在 Compiler 和 Compilation 的工作流程里，最耗时的阶段分别是哪个。对于 Compiler 实例而言，耗时最长的显然是生成编译过程实例后的 make 阶段，在这个阶段里，会执行模块编译到优化的完整过程。而对于 Compilation 实例的工作流程来说，不同的项目和配置各有不同，但总体而言，编译模块和后续优化阶段的生成产物并压缩代码的过程都是比较耗时的。</p>
<p>从这个思考题的答案中你也可以发现，不同项目的构建，在整个流程的前期初始化阶段与最后的产物生成阶段的构建时间区别不大。真正影响整个构建效率的还是 Compilation 实例的处理过程，这一过程又可分为两个阶段：编译模块和优化处理。今天我们主要讨论第一个阶段：编译模块阶段的效率提升。</p>
<h3>优化前的准备工作</h3>
<p>在进入实际优化分析之前，首先需要进行两项准备工作：</p>
<ol>
<li><strong>准备基于时间的分析工具</strong>：我们需要一类插件，来帮助我们统计项目构建过程中在编译阶段的耗时情况，这类工具可以是上一课中我们尝试手写的，也可以是使用第三方的工具。例如 <a href="https://github.com/stephencookdev/speed-measure-webpack-plugin">speed-measure-webpack-plugin</a>。</li>
<li><strong>准备基于产物内容的分析工具</strong>：从产物内容着手分析是另一个可行的方式，因为从中我们可以找到对产物包体积影响最大的包的构成，从而找到那些冗余的、可以被优化的依赖项。通常，减少这些冗余的依赖包模块，不仅能减小最后的包体积大小，也能提升构建模块时的效率。通常可以使用 <a href="https://www.npmjs.com/package/webpack-bundle-analyzer">webpack-bundle-analyzer</a> 分析产物内容。</li>
</ol>
<p>在准备好相应的分析工具后，接下来，就开始分析编译阶段的具体提效方向。编译模块阶段所耗的时间是从单个入口点开始，编译每个模块的时间的总和。要提升这一阶段的构建效率，大致可以分为三个方向（这一节课的代码示例参见 <a href="https://github.com/fe-efficiency/lessons_fe_efficiency/tree/master/11_build_efficiency">11_build_efficiency</a>）：</p>
<ol>
<li>减少执行编译的模块。</li>
<li>提升单个模块构建的速度。</li>
<li>并行构建以提升总体效率。</li>
</ol>
<h3>减少执行构建的模块</h3>
<p>提升编译模块阶段效率的第一个方向就是减少执行编译的模块。显而易见，如果一个项目每次构建都需要编译 1000 个模块，但是通过分析后发现其中有 500 个不需要编译，显而易见，经过优化后，构建效率可以大幅提升。当然，前提是找到原本不需要进行构建的模块，下面我们就来逐一分析。</p>
<h4>IgnorePlugin</h4>
<p>有的依赖包，除了项目所需的模块内容外，还会附带一些多余的模块。典型的例子是 <a href="https://www.npmjs.com/package/moment">moment</a> 这个包，一般情况下在构建时会自动引入其 locale 目录下的多国语言包，如下面的图片所示：</p>
<p><img src="assets/CgqCHl9fIKaAFpvlAAFYNtxZyV0507.png" alt="Drawing 0.png" /></p>
<p>但对于大多数情况而言，项目中只需要引入本国语言包即可。而 Webpack 提供的 IgnorePlugin 即可在构建模块时直接剔除那些需要被排除的模块，从而提升构建模块的速度，并减少产物体积，如下面的图片所示。</p>
<p><img src="assets/Ciqc1F9fILCATdbnAABZJ_SBA-k160.png" alt="Drawing 1.png" />
<img src="assets/CgqCHl9fILaAS4hfAAEWkKJEE7E961.png" alt="Drawing 2.png" /></p>
<p>除了 moment 包以外，其他一些带有国际化模块的依赖包，例如之前介绍 Mock 工具中提到的 Faker.js 等都可以应用这一优化方式。</p>
<h4>按需引入类库模块</h4>
<p>第二种典型的减少执行模块的方式是按需引入。这种方式一般适用于工具类库性质的依赖包的优化，典型例子是<a href="https://www.npmjs.com/package/lodash"> lodash </a>依赖包。通常在项目里我们只用到了少数几个 lodash 的方法，但是构建时却发现构建时引入了整个依赖包，如下图所示：</p>
<p><img src="assets/CgqCHl9fIMWAfBHWAAD0TYKbsl8944.png" alt="Drawing 3.png" /></p>
<p>要解决这个问题，效果最佳的方式是在导入声明时只导入依赖包内的特定模块，这样就可以大大减少构建时间，以及产物的体积，如下图所示。</p>
<p><img src="assets/CgqCHl9fIMyAfUzpAADukgQoyfw559.png" alt="Drawing 4.png" /></p>
<p>除了在导入时声明特定模块之外，还可以使用 babel-plugin-lodash 或 babel-plugin-import 等插件达到同样的效果。</p>
<p>另外，有同学也许会想到 <a href="https://webpack.js.org/guides/tree-shaking/">Tree Shaking</a>，这一特性也能减少产物包的体积，但是这里有两点需要注意：</p>
<ol>
<li>Tree Shaking 需要相应导入的依赖包使用 ES6 模块化，而 lodash 还是基于 CommonJS ，需要替换为 lodash-es 才能生效。</li>
<li>相应的操作是在优化阶段进行的，换句话说，Tree Shaking 并不能减少模块编译阶段的构建时间。</li>
</ol>
<h4>DllPlugin</h4>
<p>DllPlugin 是另一类减少构建模块的方式，它的核心思想是将项目依赖的框架等模块单独构建打包，与普通构建流程区分开。例如，原先一个依赖 React 与 react-dom 的文件，在构建时，会如下图般处理：</p>
<p><img src="assets/CgqCHl9fIOSAYnmjAAFH8Ofyt34986.png" alt="Drawing 5.png" />
而在通过 DllPlugin 和 DllReferencePlugin 分别配置后的构建时间就变成如下图所示，由于构建时减少了最耗时的模块，构建效率瞬间提升十倍。</p>
<p><img src="assets/CgqCHl9fIPOALYMeAAFQB_4TuTU987.png" alt="Drawing 6.png" /></p>
<h4>Externals</h4>
<p>Webpack 配置中的 externals 和 DllPlugin 解决的是同一类问题：将依赖的框架等模块从构建过程中移除。它们的区别在于：</p>
<ol>
<li>在 Webpack 的配置方面，externals 更简单，而 DllPlugin 需要独立的配置文件。</li>
<li>DllPlugin 包含了依赖包的独立构建流程，而 externals 配置中不包含依赖框架的生成方式，通常使用已传入 CDN 的依赖包。</li>
<li>externals 配置的依赖包需要单独指定依赖模块的加载方式：全局对象、CommonJS、AMD 等。</li>
<li>在引用依赖包的子模块时，DllPlugin 无须更改，而 externals 则会将子模块打入项目包中。</li>
</ol>
<p>externals 的示例如下面两张图，可以看到经过 externals 配置后，构建速度有了很大提升。</p>
<p><img src="assets/Ciqc1F9fIPiAJx62AAEEeJ5yROI594.png" alt="Drawing 7.png" />
<img src="assets/Ciqc1F9fIQSAAB3_AAD6KAV5S6M930.png" alt="Drawing 8.png" /></p>
<h3>提升单个模块构建的速度</h3>
<p>提升编译阶段效率的第二个方向，是在保持构建模块数量不变的情况下，提升单个模块构建的速度。具体来说，是通过减少构建单个模块时的一些处理逻辑来提升速度。这个方向的优化主要有以下几种：</p>
<h4>include/exclude</h4>
<p>Webpack 加载器配置中的 include/exclude，是常用的优化特定模块构建速度的方式之一。</p>
<p>include 的用途是只对符合条件的模块使用指定 Loader 进行转换处理。而 exclude 则相反，不对特定条件的模块使用该 Loader（例如不使用 babel-loader 处理 node_modules 中的模块）。如下面两张图片所示。</p>
<p><img src="assets/CgqCHl9fIQmAVCu5AAH_1DmTw5Q884.png" alt="Drawing 9.png" />
<img src="assets/CgqCHl9fIRmAYw1PAAG8nEHHA1k680.png" alt="Drawing 10.png" />
这里有两点需要注意：</p>
<ol>
<li>从上面的第二张图中可以看到，jquery 和 lodash 的编译过程仍然花费了数百毫秒，说明通过 include/exclude 排除的模块，并非不进行编译，而是使用 Webpack 默认的 js 模块编译器进行编译（例如推断依赖包的模块类型，加上装饰代码等）。</li>
<li>在一个 loader 中的 include 与 exclude 配置存在冲突的情况下，优先使用 exclude 的配置，而忽略冲突的 include 部分的配置，具体可以参照示例代码中的 webpack.inexclude.config.js。</li>
</ol>
<h4>noParse</h4>
<p>Webpack 配置中的 module.noParse 则是在上述 include/exclude 的基础上，进一步省略了使用默认 js 模块编译器进行编译的时间，如下面两张图片所示。</p>
<p><img src="assets/CgqCHl9fIR-AABfPAAGe7gdO_nc998.png" alt="Drawing 11.png" />
<img src="assets/CgqCHl9fIS2ARrYXAAFGpNGygsY433.png" alt="Drawing 12.png" /></p>
<h4>Source Map</h4>
<p>Source Map 对于构建时间的影响在第三课中已经展开讨论过，这里再稍做总结：对于生产环境的代码构建而言，会根据项目实际情况判断是否开启 Source Map。在开启 Source Map 的情况下，优先选择与源文件分离的类型，例如 &quot;source-map&quot;。有条件也可以配合错误监控系统，将 Source Map 的构建和使用在线下监控后台中进行，以提升普通构建部署流程的速度。</p>
<h4>TypeScript 编译优化</h4>
<p>Webpack 中编译 TS 有两种方式：使用 ts-loader 或使用 babel-loader。其中，在使用 ts-loader 时，由于 ts-loader 默认在编译前进行类型检查，因此编译时间往往比较慢，如下面的图片所示。</p>
<p><img src="assets/Ciqc1F9fITOAXQGlAAEcMk0PqdY814.png" alt="Drawing 13.png" />
通过加上配置项 transpileOnly: true，可以在编译时忽略类型检查，从而大大提升 TS 模块的编译速度，如下面的图片所示。</p>
<p><img src="assets/Ciqc1F9fITqAO9uoAAEDJx7jQcA803.png" alt="Drawing 14.png" />
而 babel-loader 则需要单独安装 @babel/preset-typescript 来支持编译 TS（Babel 7 之前的版本则还是需要使用 ts-loader）。babel-loader 的编译效率与上述 ts-loader 优化后的效率相当，如下面的图片所示。</p>
<p><img src="assets/CgqCHl9fIUqAGSCpAAD9Llg28C8211.png" alt="Drawing 15.png" />
不过单独使用这一功能就丧失了 TS 中重要的类型检查功能，因此在许多脚手架中往往配合 ForkTsCheckerWebpackPlugin 一同使用。</p>
<h4>Resolve</h4>
<p>Webpack 中的 resolve 配置制定的是在构建时指定查找模块文件的规则，例如：</p>
<ul>
<li><strong>resolve.modules</strong>：指定查找模块的目录范围。</li>
<li><strong>resolve.extensions</strong>：指定查找模块的文件类型范围。</li>
<li><strong>resolve.mainFields</strong>：指定查找模块的 package.json 中主文件的属性名。</li>
<li><strong>resolve.symlinks</strong>：指定在查找模块时是否处理软连接。</li>
</ul>
<p>这些规则在处理每个模块时都会有所应用，因此尽管对小型项目的构建速度来说影响不大，但对于大型的模块众多的项目而言，这些配置的变化就可能产生客观的构建时长区别。例如下面的示例就展示了使用默认配置和增加了大量无效范围后，构建时长的变化情况：</p>
<p><img src="assets/CgqCHl9fIU-AGs1fAAErO09KCQg428.png" alt="Drawing 16.png" />
<img src="assets/Ciqc1F9fIWCAKxMyAAErVYo_MgQ418.png" alt="Drawing 17.png" /></p>
<h3>并行构建以提升总体效率</h3>
<p>第三个编译阶段提效的方向是使用并行的方式来提升构建的效率。并行构建的方案早在 Webpack 2 时代已经出现，随着目前最新稳定版本 Webpack 4 的发布，人们发现在一般项目的开发阶段和小型项目的各构建流程中<a href="https://blog.johnnyreilly.com/2018/12/you-might-not-need-thread-loader.html">已经用不到这种并发的思路</a>了，因为在这些情况下，并发所需要的多进程管理与通信所带来的额外时间成本可能会超过使用工具带来的收益。但是在大中型项目的生产环境构建时，这类工具仍有发挥作用的空间。这里我们介绍两类并行构建的工具： HappyPack 与 thread-loader，以及 parallel-webpack。</p>
<h4>HappyPack 与 thread-loader</h4>
<p>这两种工具的本质作用相同，都作用于模块编译的 Loader 上，用于在特定 Loader 的编译过程中，以开启多进程的方式加速编译。HappyPack 诞生较早，而 thread-loader 参照它的效果实现了更符合 Webpack 中 Loader 的编写方式。下面就以 thread-loader 为例，来看下应用前后的构建时长对比，如下面的两张图所示。</p>
<p><img src="assets/CgqCHl9fIWaAKvjDAAGxNVse3m4379.png" alt="Drawing 18.png" />
<img src="assets/Ciqc1F9fIXOAHx6XAAIyabhj3_g078.png" alt="Drawing 19.png" /></p>
<h4>parallel-webpack</h4>
<p>并发构建的第二种场景是针对与多配置构建。Webpack 的配置文件可以是一个包含多个子配置对象的数组，在执行这类多配置构建时，默认串行执行，而通过 parallel-webpack，就能实现相关配置的并行处理。从下图的示例中可以看到，通过不同配置的并行构建，构建时长缩短了 30%：</p>
<p><img src="assets/CgqCHl9fIXuARXhnAADx6PzQuE0879.png" alt="Drawing 20.png" />
<img src="assets/Ciqc1F9fIbCAL6knAAEbXZ1tRpw256.png" alt="Drawing 21.png" /></p>
<h3>总结</h3>
<p>这节课我们整理了 Webpack 构建中编译模块阶段的构建效率优化方案。对于这一阶段的构建效率优化可以分为三个方向：以减少执行构建的模块数量为目的的方向、以提升单个模块构建速度为目的的方向，以及通过并行构建以提升整体构建效率的方向。每个方向都包含了若干解决工具和配置。</p>
<p>今天课后的<strong>思考题是</strong>：你的项目中是否都用到了这些解决方案呢？希望你结合课程的内容，和所开发的项目中用到的优化方案进行对比，查漏补缺。如果有这个主题方面其他新的解决方案，也欢迎在留言区讨论分享。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;&#32;流程分解：Webpack&#32;的完整构建流程.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;&#32;打包提效：如何为&#32;Webpack&#32;打包阶段提速？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4351ff3cf1645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
