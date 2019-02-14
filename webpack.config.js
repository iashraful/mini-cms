let path = require('path');
let webpack = require('webpack');
const MinifyPlugin = require('babel-minify-webpack-plugin');

function resolve(dir) {
    return path.join(__dirname, dir)
}

// Directory for deployed assets. It should be within our static files path.
// Backslash at the end is not required.
let distDir = '/cms/static/dist';
let pluginsList = [];
if (process.env.NODE_ENV === 'production') {
    pluginsList.push(
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new MinifyPlugin()
    )
}
let entryFile = {
    main: './cms/client/main.js',
    extra: './cms/client/extra-chunks',
    admin: './cms/client/admin/main.js'

};

module.exports = {
    entry: entryFile,
    output: {
        path: path.resolve(__dirname, '.' + distDir + '/'),
        filename: '[name]-bundle.min.js'
    },
    plugins: pluginsList,
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
                        // the "scss" and "sass" values for the lang attribute to the right configs here.
                        // other preprocessors should work out of the box, no loader config like this nessessary.
                        'scss': 'vue-style-loader!css-loader!sass-loader',
                        'sass': 'vue-style-loader!css-loader!sass-loader?indentedSyntax'
                    }
                    // other vue-loader options go here
                }
            },
            {
                test: /\.scss$/,
                use: [
                    'style-loader', // creates style nodes from JS strings
                    'css-loader', // translates CSS into CommonJS
                    'sass-loader' // compiles Sass to CSS, using Node Sass by default
                ]
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /^(?!.*?\.module).*\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.module\.css$/,
                use: ['style-loader', {
                    loader: 'css-loader',
                    options: {
                        modules: true
                    }
                }]
            },
            {
                test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {name: 'static/media/[name].[ext]?[hash]'}
                    }
                ]
            },
            {
                test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url?limit=10000&mimetype=application/font-woff'
            },
            {
                test: /\.tff(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url-loader?limit=10000&mimetype=application/octet-stream'
            },
            {
                test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'file-loader'
            },
            {
                test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url-loader?limit=10000&mimetype=image/svg+xml'
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            '@': resolve('cms/client')
        }
    }
};
