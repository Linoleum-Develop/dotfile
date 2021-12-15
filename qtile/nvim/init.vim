syntax on

set mouse=a
set noerrorbells
set sw=2
set expandtab
set smartindent
set number
set rnu
set numberwidth=1
set noswapfile
set incsearch
set ignorecase
set clipboard=unnamedplus
set encoding=utf-8
set cursorline
set termguicolors

set colorcolumn=120
highlight ColoColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/.local/share/nvim/plugged')

"themes
Plug 'morhetz/gruvbox'
Plug 'ayu-theme/ayu-vim'
Plug 'joshdick/onedark.vim'
Plug 'abra/vim-obsidian'

"visual
Plug 'yggdroot/indentline'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'ryanoasis/vim-devicons'
Plug 'lilydjwg/colorizer'
Plug 'leafgarland/typescript-vim'

"Git integration
Plug 'mhinz/vim-signify'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'
Plug 'junegunn/gv.vim'

"Funtionality
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'KabbAmine/vCoolor.vim'
Plug 'easymotion/vim-easymotion'
Plug 'rust-lang/rust.vim'
Plug 'cespare/vim-toml'
Plug 'vim-python/python-syntax'

"Code completion
Plug 'ddollar/nerdcommenter'
Plug 'honza/vim-snippets'
Plug 'sirver/ultisnips'
Plug 'jiangmiao/auto-pairs'
Plug 'mattn/emmet-vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()
"theme

let g:python_highlight_all = 1
set termguicolors
set background=dark
let ayucolor="dark"
let g:gruvbox_cotrast_dark="hard"
colorscheme gruvbox

let mapleader = " "
